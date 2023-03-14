import hashlib
import socket
from dataBase import UserData


class Client:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port
        self.client = None

    def connect(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.server_ip, self.server_port))
        message = self.client.recv(1024).decode()
        self.client.send(input(message).encode())
        message = self.client.recv(1024).decode()
        self.client.send(input(message).encode())
        print(self.client.recv(1024).decode())

    def login(self, username, password):
        # TODO: Implement login logic here
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if username == UserData.username1 and hashed_password == UserData.hashed_password1:
            return "Login Processed"
        else:
            return False


class LoginSystem:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port
        self.client = None

    def login(self):
        if not self.client:
            self.client = Client(self.server_ip, self.server_port)
            self.client.connect()

        username = self.entry1.get()
        password = self.entry2.get()

        response = self.client.login(username, password)

        if response == "Login Processed":
            print("Login Successful")
        else:
            print("Login Failed")
