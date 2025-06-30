class Products:
    def __init__(self):
        self.db = []

    def insert(self, data):
        self.db.append(data)
        return "Produto cadastrado com sucesso"
