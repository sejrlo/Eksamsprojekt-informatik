import socket
import threading 
import json
from Server import *


requests = {"Register":register, "Login":login, "create_media":create_media, "get_media":get_media, "del_media":del_media, "Search":search}

class Connection:
    def __init__(self, requests, header=64, port=5050, server="0.0.0.0", format='utf-8', disconnect_msg="!DISCONNECT"):
        self.HEADER = header
        self.PORT = port
        self.SERVER = server
        self.ADDR = (self.SERVER, self.PORT)
        self.FORMAT = format
        self.DISCONNECT_MSG = disconnect_msg


        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1) 
        self.server.bind(self.ADDR)

        self.requests = requests

    def send_message(self, conn, data):
        message = json.dumps(data).encode(self.FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(self.FORMAT)
        send_length += b' ' * (self.HEADER - len(send_length))

        conn.send(send_length)
        conn.send(message)

    def receive_message(self, conn):
        msg_length = conn.recv(self.HEADER).decode(self.FORMAT)
        if msg_length: 
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(self.FORMAT)
            
            return msg

        return ""

    def handle_client(self, conn, addr):
        print(f"[NEW CONNECTION] {addr} connected.")

        connection_context = {"userID":-1}
        
        while True:
            msg = self.receive_message(conn)
            if msg == "": continue
            if msg == self.DISCONNECT_MSG: break
            print(f"[{addr}] {msg}")
            print(msg)
            data = json.loads(msg)
            print(data, type(data))
            new_data, response = self.requests[data["request"]](data, connection_context)
            if response["request"] == "login" or response["request"] == "login":
                if response["status"] == "success": connection_context["userID"] = new_data["userID"]
            
            self.send_message(conn, response)

        conn.close()

    def start(self):
        self.server.listen(1)
        print(f"[LISTENING] Server is listening on {self.SERVER}")
        try:
            while True:
                conn, addr = self.server.accept()
                thread = threading.Thread(target=self.handle_client, args=(conn, addr))
                thread.daemon = True
                thread.start()
                print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
        except KeyboardInterrupt: 
            pass

connection = Connection(requests)
connection.start()