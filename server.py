import sqlite3
import hashlib
import socket
import threading

class Server:
    def __init__(self):
        # creating a tcp connection
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(("", "")) #you can put your host ip and the port number
        self.server.listen()

    # TODO:add encryption to the data itself and secure the connection and solve vulnerability to sql injection

    # take a client as c to handle each client's request
    def client_handler(self, c):
        c.send("Username: ".encode())
        self.username = c.recv(1024).decode()
        c.send("Password: ".encode())
        self.password = c.recv(1024)
        self.password = hashlib.sha256(self.password).hexdigest()

        self.conn = sqlite3.connect("user_data.db")
        self.cur = self.conn.cursor()

        self.cur.execute("SELECT * FROM user_data WHERE username=? AND password=?", (self.username, self.password))

        if self.cur.fetchall():
            c.send("Login Processed".encode())
            # TODO:secrets and then services that you want to give to the client
        else:
            c.send("Login Failed".encode())


    def start_server(self):
        while True:
            client, addr = self.server.accept()
            client_thread = threading.Thread(target=self.client_handler, args=(client,))
            client_thread.start()

if __name__ == '__main__':
    server = Server()
    server.start_server()
