class Ticket:
    def __init__(self, db):
        self.db = db

    def save(self, table, data):
        self.db.insert(table, data)

    def show(self, table, columns=None):
        return self.db.select(table, columns)

    def show_one(self, table, id, columns=None):
        return self.db.select_id(table, id, columns)

    def update(self, table, id, data):
        self.db.update(table, id, data)

    def delete(self, table, id):
        self.db.delete(table, id)
