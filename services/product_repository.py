from database.products import Products

class ProductRepository:
    def add_product(self, data):
        # validações aqui
        return Products().insert(data)
