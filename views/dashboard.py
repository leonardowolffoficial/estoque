from security.permission_manager import PermissionManager

class Dashboard:
    def show(self, user):
        if PermissionManager().has_access(user, "dashboard"):
            print("Exibindo Dashboard...")
        else:
            print("Acesso negado.")
