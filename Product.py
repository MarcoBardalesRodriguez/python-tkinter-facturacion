from Model.Database import Database
from Model.ModelProduct import Product as ModelProduct
from Controller.ControllerProduct import Product as ControllerProduct
from View.ViewProduct import Product as ViewProduct

db = Database('db.db', 'schema.sql')

model_product = ModelProduct(db)
view_product = ViewProduct()
controller_product = ControllerProduct(model_product, view_product)
view_product.set_controller(controller_product)


class Product:
    def __init__(self):
        global view_product
        self.view = view_product

    def new_product(self):
        name = input("nombre: ")
        stock = int(input("stock: "))
        price = float(input("precio: "))

        data = [
                {'nombre': name, 'stock': stock, 'precio': price}
            ]

        self.view.save('producto', data)

    def show_products(self):
        self.view.show('producto', ['id', 'nombre', 'stock', 'precio'])

    def update_product(self):
        id = int(input("id: "))
        name = input("nombre: ")
        stock = int(input("stock: "))
        price = float(input("precio: "))

        data = [
            {'nombre': name, 'stock': stock, 'precio': price}
        ]

        self.view.update('producto', id, data)

    def delete_product(self):
        valor = int(input("id: "))
        id = {'id': valor}
        self.view.delete('producto', id)
