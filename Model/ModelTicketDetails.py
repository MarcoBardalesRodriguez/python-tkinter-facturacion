class TicketDetails:
    def __init__(self, db):
        self.db = db

    def save(self, table, data):
        self.db.insert(table, data)

    def show(self, ticket_id):
        self.db.connect()
        query = f"""
        SELECT
        B.id as boleta,
        D.cantidad as cantidad,
        P.nombre as producto,
        P.precio as precio
        FROM boleta B
            JOIN detalle_boleta D on D.boleta_id = B.id
            JOIN producto P on D.producto_id = P.id
        WHERE B.id = {ticket_id};
        """
        return self.db.query_with_return(query)

    def delete(self, table, id):
        self.db.delete(table, id)
