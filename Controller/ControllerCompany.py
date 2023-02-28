class Company:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show(self, table, columns=None):
        self.view.message("cargando")
        return self.model.show(table, columns)

    def update(self, table, id, data):
        self.model.update(table, id, data)
        self.view.message("actualizado")
