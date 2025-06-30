from database.users import Users

class AuthManager:
    def authenticate(self, username, password):
        return Users().check_credentials(username, password)
