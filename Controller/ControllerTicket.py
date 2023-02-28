class Ticket:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def save(self, table, data):
        self.model.save(table, data)
        self.view.message("guardado")

    def show(self, table, columns=None):
        self.view.message("cargando")
        return self.model.show(table, columns)

    def update(self, table, id, data):
        self.model.update(table, id, data)
        self.view.message("actualizado")

    def delete(self, table, id):
        self.model.delete(table, id)
        self.view.message("eliminado")
