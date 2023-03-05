class Ticket:
    def __init__(self):
        self._controller = None

    def set_controller(self, controller):
        self._controller = controller

    def message(self, message):
        print(message)

    def save(self, table, data):
        self._controller.save(table, data)

    def show(self, table, columns=None):
        res = self._controller.show(table, columns)
        for row in res:
            print(row)
        return res

    def show_one(self, table, id, columns=None):
        res = self._controller.show_one(table, id, columns)
        for row in res:
            print(row)
        return res

    def update(self, table, id, data):
        self._controller.update(table, id, data)

    def delete(self, table, id):
        self._controller.delete(table, id)