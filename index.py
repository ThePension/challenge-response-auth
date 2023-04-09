from client import Client
from server import Server

if __name__ == '__main__':
    server = Server()
    client = Client("toto", "pwd", server)
    
    # Tentative de connexion de l'utilisateur
    # Lors de cette tentative, le serveur envoie un nonce au client
    # Le client doit alors résoudre le challenge et renvoyer le résultat au serveur
    if client.login():
        print("User logged in")
    else:
        print("User not logged in")