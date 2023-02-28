class TicketDetails:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def save(self, table, data):
        self.model.save(table, data)
        self.view.message("guardado")

    def show(self,ticket_id):
        self.view.message("cargando")
        return self.model.show(ticket_id)

    def delete(self, table, id):
        self.model.delete(table, id)
        self.view.message("eliminado")
