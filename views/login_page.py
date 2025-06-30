from security.auth_manager import AuthManager

class LoginPage:
    def login(self, username, password):
        auth = AuthManager()
        if auth.authenticate(username, password):
            print("Login bem-sucedido!")
            return True
        else:
            print("Credenciais inválidas.")
            return False
