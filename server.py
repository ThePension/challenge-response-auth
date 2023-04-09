import random
import hashlib
import secrets

users = {
    "toto": "pwd", # hashlib.sha256("pwd".encode()).hexdigest(),
    "user2": hashlib.sha256("pass2".encode()).hexdigest()
}


class Server:
    def __init__(self):
        # Store a list of authenticated users
        self.auth_users = []
        
        # Store a list of pending auth users with their corresponding nonce
        self.pending_auth = {}
        
    def get_nonce(self, username):
        # If user is already logged in, return False
        if username in self.auth_users:
            return False
        
        # Generate a random nonce using secrets.SystemRandom
        nonce = secrets.SystemRandom().randint(0, 1000000)
        
        # Store the nonce, waiting for the user to send it back
        self.pending_auth.update({username: nonce})
        
        return nonce
        
    def login(self, username, cnonce, challenge_result=None):
        # If user is already logged in, return False
        if username in self.auth_users:
            print("User already logged in")
            return False
        
        # If the user does not exist, return False
        if username not in users.keys():
            print("User does not exist")
            return False
                
        # Check if the challenge result is correct
        if challenge_result == self.solve_challenge(username, cnonce):
            self.auth_users.append(username)
            print("Welcome " + username)
            return True
        else:
            print("Wrong challenge result")
            print("Expected: " + self.solve_challenge(username, cnonce))
            print("Got: " + challenge_result)
            return False

    def solve_challenge(self, username, cnonce):
        # Get the nonce from the pending auth list
        nonce = self.pending_auth[username]
        
        # Get the user password
        password = users[username]
        
        print("Received cnonce: " + str(cnonce))
        print("Received nonce: " + str(nonce))
        print("User password: " + password)
        
        return hashlib.sha256((str(nonce) + str(cnonce) + password).encode()).hexdigest()