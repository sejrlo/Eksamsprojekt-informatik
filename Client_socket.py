import socket
import json

ip = "127.0.0.1"

class Connection:
    def __init__(self):
        self.SERVER = ip
        self.PORT = 5050
        self.ADDR = (self.SERVER, self.PORT)
        self.HEADER = 64
        self.FORMAT = 'ascii'
        self.DISCONNECT_MSG = "!DISCONNECT"
        
        
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
