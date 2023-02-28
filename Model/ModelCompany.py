class Company:
    def __init__(self, db):
        self.db = db
        init_values = "(1, \'ruc\', \'nombre\', \'direccion\', \'celular\', \'email\')"
        query = f"INSERT OR IGNORE INTO empresa VALUES {init_values};"
        self.db.query_without_return(query)

    def show(self, table, columns=None):
        return self.db.select(table, columns)

    def update(self, table, id, data):
        self.db.update(table, id, data)
