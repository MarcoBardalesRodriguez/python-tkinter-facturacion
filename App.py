import tkinter as tk
from tkinter import ttk
from Ticket import Ticket
from Product import Product
from Company import Company
from TicketDetails import TicketDetails


class App(tk.Tk):
    global ticket
    global product
    global company
    global ticket_details

    def __init__(self):
        super().__init__()

        self.title('Facturacion')
        self.geometry('800x600')
        self.resizable(False, False)

        # Crear el menú
        self.menu_bar = tk.Menu(self)
        self.config(menu=self.menu_bar)

        # Crear las opciones del menú
        self.menu_bar.add_command(label='Boletas', command=self.frame_ticket)
        self.menu_bar.add_command(label='Productos', command=self.frame_product)
        self.menu_bar.add_command(label='Empresa', command=self.frame_company)
        self.menu_bar.add_command(label='Salir', command=self.salir)

        # Crear el frame principal
        self.main_frame = ttk.Frame(self)
        self.main_frame.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

        # Agregar un label al frame principal
        self.main_label = ttk.Label(self.main_frame, text='Inicio')
        self.main_label.pack(expand=True)

    def frame_ticket(self):
        # Crear el frame para la opción "Boletas"
        self.main_frame.destroy()
        self.main_frame = ttk.Frame(self)
        self.main_frame.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

        # Agregar un label al frame de "Boletas"
        self.ticket_label = ttk.Label(self.main_frame, text='Boletas')
        self.ticket_label.pack(expand=True)

    def frame_product(self):
        # Crear el frame para la opción "Productos"
        self.main_frame.destroy()
        self.main_frame = ttk.Frame(self)
        self.main_frame.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

        # Agregar un label al frame de "Productos"
        self.product_label = ttk.Label(self.main_frame, text='Productos')
        self.product_label.pack(expand=True)

    def frame_company(self):
        # Crear el frame para la opción "Empresa"
        self.main_frame.destroy()
        self.main_frame = ttk.Frame(self)
        self.main_frame.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

        # Agregar un label al frame de "Empresa"
        self.company_label = ttk.Label(self.main_frame, text='Empresa')
        self.company_label.pack(expand=True)

        # Obtener los datos de la "Empresa"
        id, ruc, name, address, phone, email = company.show_company()

        company_ruc = ttk.Label(self.main_frame, text='Ruc')
        company_ruc.pack(padx=5, pady=5)
        new_ruc = ttk.Entry(self.main_frame, width=30)
        new_ruc.insert(0, ruc)
        new_ruc.pack(padx=5, pady=5)

    def salir(self):
        self.quit()


if __name__ == '__main__':
    ticket = Ticket()
    product = Product()
    company = Company()
    ticket_details = TicketDetails()
    app = App()
    app.mainloop()
