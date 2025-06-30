class Users:
    def __init__(self):
        self.users = {"admin": "1234"}

    def check_credentials(self, username, password):
        return self.users.get(username) == password
