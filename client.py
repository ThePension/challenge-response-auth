import hashlib
import random
import secrets


class Client:
    def __init__(self, username, password, server):
        self.username = username
        self.password = password
        self.server = server
        self.is_logged_in = False
        
    def login(self):
        # Request login and get the nonce
        nonce = self.request_login()
        
        # Generate a random cnonce using secrets module
        cnonce = secrets.SystemRandom().randint(0, 1000000)
        
        # Resolve challenge (hash the nonce)
        challenge_result = self.resolve_challenge(nonce, cnonce)
        
        # Send it back to the server
        self.is_logged_in = self.send_resolved_challenge(challenge_result, cnonce)
        
        return self.is_logged_in
        
    def request_login(self):
        return self.server.get_nonce(self.username)

    def resolve_challenge(self, nonce, cnonce=None):
        # Result = hash(nonce + cnonce + password), as described in : https://en.wikipedia.org/wiki/Cryptographic_nonce
        return hashlib.sha256((str(nonce) + str(cnonce) + self.password).encode()).hexdigest()

    def send_resolved_challenge(self, challenge_result, cnonce=None):
        return self.server.login(self.username, cnonce, challenge_result)