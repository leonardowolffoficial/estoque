from services.product_repository import ProductRepository

class ProductController:
    def __init__(self):
        self.repo = ProductRepository()

    def create_product(self, data):
        return self.repo.add_product(data)
