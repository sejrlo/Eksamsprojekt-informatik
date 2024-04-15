import socket
import json

ip = "127.0.0.1"

class Connection:
    def __init__(self, server = ip, port = 5050, header = 64, format = 'utf-8', disconnect = "!DISCONNECT"):
        self.SERVER = server
        self.PORT = port
        self.ADDR = (self.SERVER, self.PORT)
        self.HEADER = header
        self.FORMAT = format
        self.DISCONNECT_MSG = disconnect
        
        
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.ADDR)

    def send(self, msg):
        message = json.dumps(msg).encode(self.FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(self.FORMAT)
        send_length += b' ' * (self.HEADER - len(send_length))

        self.client.send(send_length)
        self.client.send(message)

    def receive(self): 
        msg_length = self.client.recv(self.HEADER).decode(self.FORMAT)
        msg = self.client.recv(int(msg_length)).decode(self.FORMAT)
        return json.loads(msg)

    def disconnect(self):
        message = self.DISCONNECT_MSG.encode(self.FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(self.FORMAT)
        send_length += b' ' * (self.HEADER - len(send_length))

        self.client.send(send_length)
        self.client.send(message)
