from Model.Database import Database
from Model.ModelCompany import Company as ModelCompany
from Controller.ControllerCompany import Company as ControllerCompany
from View.ViewCompany import Company as ViewCompany

db = Database('db.db', 'schema.sql')

model_company = ModelCompany(db)
view_company = ViewCompany()
controller_company = ControllerCompany(model_company, view_company)
view_company.set_controller(controller_company)


class Company:
    def __init__(self):
        global view_company
        self.view = view_company

    def show_company(self):
        return self.view.show('empresa', ['id', 'ruc', 'nombre', 'direccion', 'celular', 'email'])

    def update_company(self, id, ruc, name, address, phone, email):
        # id = 1
        # ruc = input("ruc: ")
        # name = input("nombre: ")
        # address = input("direccion: ")
        # phone = input("celular: ")
        # email = input("email: ")

        data = [
            {'ruc': ruc, 'nombre': name, 'direccion': address, 'celular': phone, 'email': email}
        ]

        self.view.update('empresa', id, data)
