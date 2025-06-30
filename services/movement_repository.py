from database.movements import Movements

class MovementRepository:
    def add_movement(self, product_id, quantity, tipo):
        # regra de negócio, validações etc
        return Movements().record(product_id, quantity, tipo)
