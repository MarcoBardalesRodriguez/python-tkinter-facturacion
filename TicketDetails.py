from Model.Database import Database
from Model.ModelTicketDetails import TicketDetails as ModelTicketDetails
from Controller.ControllerTicketDetails import TicketDetails as ControllerTicketDetails
from View.ViewTicketDetails import TicketDetails as ViewTicketDetails

db = Database('db.db', 'schema.sql')

model_ticket_details = ModelTicketDetails(db)
view_ticket_details = ViewTicketDetails()
controller_ticket_details = ControllerTicketDetails(model_ticket_details, view_ticket_details)
view_ticket_details.set_controller(controller_ticket_details)


class TicketDetails:
    def __init__(self):
        global view_ticket_details
        self.view = view_ticket_details

    def new_ticket_details(self, details: list[dict]):
        # details = [{'boleta_id': ticket_id, 'producto_id': product_id, 'cantidad': quantity},
        #            {'boleta_id': ticket_id, 'producto_id': product_id, 'cantidad': quantity},
        #            ...]
        self.view.save('detalle_boleta', details)

    def show_ticket_details(self, id):
        return self.view.show(id)

    def delete_ticket_details(self, id):
        # id = {'boleta_id': valor}
        self.view.delete('detalle_boleta', id)

    def update_ticket_details(self):
        self.delete_ticket_details()
        self.new_ticket_details()