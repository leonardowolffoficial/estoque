class Movements:
    def __init__(self):
        self.movimentos = []

    def record(self, product_id, quantity, tipo):
        movimento = {"produto": product_id, "quantidade": quantity, "tipo": tipo}
        self.movimentos.append(movimento)
        return "Movimentação registrada"
