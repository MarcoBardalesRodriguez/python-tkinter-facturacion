from Model.Database import Database
from Model.ModelTicket import Ticket as ModelTicket
from Controller.ControllerTicket import Ticket as ControllerTicket
from View.ViewTicket import Ticket as ViewTicket

db = Database('db.db', 'schema.sql')

model_ticket = ModelTicket(db)
view_ticket = ViewTicket()
controller_ticket = ControllerTicket(model_ticket, view_ticket)
view_ticket.set_controller(controller_ticket)


class Ticket:
    def __init__(self):
        global view_ticket
        self.view = view_ticket

    def new_ticket(self):
        date = input("fecha: ")
        name = input("nombre: ")
        address = input("direccion: ")
        dni = input("dni: ")

        data = [
                {'fecha': date, 'nombre': name, 'direccion': address, 'dni': dni}
            ]

        self.view.save('boleta', data)

    def show_tickets(self):
        self.view.show('boleta', ['id', 'fecha', 'nombre', 'direccion', 'dni'])

    def update_ticket(self):
        id = int(input("id: "))
        date = input("fecha: ")
        name = input("nombre: ")
        address = input("direccion: ")
        dni = input("dni: ")

        data = [
            {'fecha': date, 'nombre': name, 'direccion': address, 'dni': dni}
        ]

        self.view.update('boleta', id, data)

    def delete_ticket(self):
        valor = int(input("id: "))
        id = {'id': valor}
        self.view.delete('boleta', id)
