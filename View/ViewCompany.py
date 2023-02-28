class Company:
    def __init__(self):
        self._controller = None

    def set_controller(self, controller):
        self._controller = controller

    def message(self, message):
        print(message)

    def show(self, table, columns=None):
        for row in self._controller.show(table, columns):
            print(row)

    def update(self, table, id, data):
        self._controller.update(table, id, data)
