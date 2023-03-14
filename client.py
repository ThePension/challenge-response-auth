class Client:
    def __init__(self, username, password, server):
        self.username = username
        self.password = password
        self.server = server
        self.is_logged_in = False
        
    def login(self):
        # Request login and get the nonce
        nonce = self.request_login()
        
        # Resolve challenge (hash the nonce)
        challenge_result = self.resolve_challenge(nonce)
        
        # Send it back to the server
        self.is_logged_in = self.send_resolved_challenge(challenge_result)
        
        if self.is_logged_in:
            print("Login successful")
        else:
            print("Login failed")
        
    def request_login(self):
        return self.server.login(self.username)

    def resolve_challenge(self, nonce):
        # Apply operations
        return nonce + 1

    def send_resolved_challenge(self, challenge_result):
        return self.server.login(self.username, challenge_result)