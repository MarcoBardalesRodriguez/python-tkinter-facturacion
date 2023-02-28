class TicketDetails:
    def __init__(self):
        self._controller = None

    def set_controller(self, controller):
        self._controller = controller

    def message(self, message):
        print(message)

    def save(self, table, data):
        self._controller.save(table, data)

    def show(self, ticket_id):
        for row in self._controller.show(ticket_id):
            print(row)

    def delete(self, table, id):
        self._controller.delete(table, id)