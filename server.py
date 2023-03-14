import random

class Server:
    def __init__(self):
        # Store a list of authenticateds 
        self.users = []
        
        # Store a list of pending auth users with their corresponding nonce
        self.pending_auth = {}
        
    def login(self, username, challenge_result=None):
        # If user is already logged in, return False
        if username in self.users:
            return False
       
        if challenge_result is None:
            # Generate a random nonce
            nonce = random.randint(0, 100)
            
            # Store the nonce, waiting for the user to send it back
            self.pending_auth.update({username: nonce})
            
            return nonce
        else:           
            # Check if the challenge result is correct
            if challenge_result == self.solve_challenge(self.pending_auth[username]):
                self.users.append(username)
                return True
            else:
                return False

    def solve_challenge(self, nonce):
        return nonce + 1