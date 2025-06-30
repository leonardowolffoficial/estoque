from services.movement_repository import MovementRepository

class InventoryController:
    def __init__(self):
        self.repo = MovementRepository()

    def record_entry(self, product_id, quantity):
        return self.repo.add_movement(product_id, quantity, "entrada")

    def record_exit(self, product_id, quantity):
        return self.repo.add_movement(product_id, quantity, "saida")
