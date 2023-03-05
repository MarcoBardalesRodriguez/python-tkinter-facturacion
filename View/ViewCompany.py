class Company:
    def __init__(self):
        self._controller = None

    def set_controller(self, controller):
        self._controller = controller

    def message(self, message):
        print(message)

    def show(self, table, columns=None):
        res = self._controller.show(table, columns)
        for row in res:
            print(row)
        return res

    def update(self, table, id, data):
        self._controller.update(table, id, data)
