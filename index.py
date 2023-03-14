from client import Client
from server import Server

if __name__ == '__main__':
    server = Server()
    client = Client("toto", "pwd", server)
    
    client.login()