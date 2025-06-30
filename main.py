from views.login_page import LoginPage
from views.dashboard import Dashboard
from controllers.product_controller import ProductController
from controllers.inventory_controller import InventoryController

def main():
    # Login
    login = LoginPage()
    if login.login("admin", "1234"):
        Dashboard().show("admin")

        # === CHAMANDO OUTRAS "ROTAS" ===
        
        # Criar um novo produto
        produto_ctrl = ProductController()
        novo_produto = {"id": 1, "nome": "Teclado Gamer", "preco": 120.0}
        print(produto_ctrl.create_product(novo_produto))

        # Entrada de estoque
        estoque_ctrl = InventoryController()
        print(estoque_ctrl.record_entry(product_id=1, quantity=10))

        # Saída de estoque
        print(estoque_ctrl.record_exit(product_id=1, quantity=2))

if __name__ == "__main__":
    main()
