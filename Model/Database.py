import sqlite3


class Database:
    def __init__(self, db, schema):
        self.conn = None
        self.cursor = None
        self.db_file = db
        self.schema_file = schema
        self.create_tables()

    def connect(self):
        self.conn = sqlite3.connect(self.db_file)
        self.cursor = self.conn.cursor()

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None

    def create_tables(self):
        self.connect()
        try:
            with open(self.schema_file, 'r') as f:
                schema = f.read()
                queries = schema.split(';')
                for query in queries:
                    self.cursor.execute(f"""{query}""")
            print("Archivo SQL ejecutado correctamente.")
        except sqlite3.Error as e:
            print("Error al ejecutar el archivo SQL:", e)
        finally:
            self.close()

    def insert(self, table: str, data: list[dict]):
        self.connect()
        columns = ', '.join(data[0].keys())
        # print(columns)
        placeholders = ', '.join(['?' for _ in data[0].keys()])
        query = f'INSERT INTO {table} ({columns}) VALUES ({placeholders})'
        for fila in data:
            values = list(fila.values())
            self.cursor.execute(query, values)
        self.conn.commit()
        self.close()

    def select(self, table: str, columns: list = None):
        self.connect()
        if columns:
            columns_names = ', '.join(columns)
        else:
            columns_names = '*'
        query = f'SELECT {columns_names} FROM {table}'
        res = self.cursor.execute(query)
        return res.fetchall()

    def select_id(self, table: str, id: int, columns: list = None):
        self.connect()
        if columns:
            columns_names = ', '.join(columns)
        else:
            columns_names = '*'
        query = f'SELECT {columns_names} FROM {table} WHERE boleta_id={id}'
        res = self.cursor.execute(query)
        return res.fetchall()

    def update(self, table: str, id: int, data: list[dict]):
        self.connect()
        format_data = ', '.join([f'{key}={repr(value)}' for key, value in data[0].items()])
        query = f'UPDATE {table} SET {format_data} WHERE id={id}'
        self.cursor.execute(query)
        self.conn.commit()
        self.close()

    def delete(self, table: str, id: dict):
        self.connect()
        query = f'DELETE FROM {table} WHERE {list(id.keys())[0]}={list(id.values())[0]}'
        self.cursor.execute(query)
        self.conn.commit()
        self.close()

    def query_with_return(self, query):
        self.connect()
        res = self.cursor.execute(query)
        return res.fetchall()

    def query_without_return(self, query):
        self.connect()
        query = query
        self.cursor.execute(query)
        self.conn.commit()
        self.close()