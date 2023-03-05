import tkinter as tk
from datetime import datetime
from tkinter import ttk, PhotoImage, Label
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
        self.main_frame = tk.Frame(self)
        self.main_frame.configure(background='white')
        self.main_frame.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

        # ruta absoluta.
        self.imagen = PhotoImage(file="home.png")
        Label(self.main_frame, image=self.imagen, bd=0).grid(row=0, column=0, padx=140, pady=35)

    def frame_ticket(self):
        def delete_ticket(id):
            ticket.delete_ticket({'id': id})
            ticket_details.delete_ticket_details({'boleta_id': id})

        # Crear el frame para la opción "Boletas"
        self.main_frame.destroy()
        self.main_frame = ttk.Frame(self)
        self.main_frame.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

        # Agregar un label al frame de "Boletas"
        self.ticket_label = ttk.Label(self.main_frame, text='Boletas')
        self.ticket_label.grid(row=0, column=0, columnspan=2, pady=10)
        button = ttk.Button(self.main_frame, text="nuevo", command=self.frame_ticket_template)
        button.grid(row=1, column=0, columnspan=2, pady=10)

        # Obtener tickets
        tickets = ticket.show_tickets()
        last_row = 3
        for item in tickets:
            last_row = last_row + 1
            id, date, name, *_ = item
            ticket_summary = ttk.Label(self.main_frame, text=f'{date}\t{name}', width=80, borderwidth=1, relief="solid")
            ticket_summary.grid(row=last_row, column=0, pady=10)
            ticket_edit = ttk.Button(self.main_frame, text='Ver/Editar', command=lambda id=id: self.frame_ticket_template(id))
            ticket_edit.grid(row=last_row, column=1, pady=10)
            ticket_delete = ttk.Button(self.main_frame, text='Eliminar', command=lambda id=id: [delete_ticket(id), self.frame_ticket()])
            ticket_delete.grid(row=last_row, column=2, pady=10)

    def frame_ticket_template(self, id: int = None):
        def create_row(frame, row, detail):
            print(detail, row)
            _, quantity, name, price = detail

            detail_quantity = ttk.Entry(frame, width=30)
            detail_quantity.insert(0, quantity)
            detail_quantity.grid(row=row, column=0, sticky="ew")
            detail_quantity.config(state="readonly")

            detail_name = ttk.Entry(frame, width=50)
            detail_name.insert(0, name)
            detail_name.grid(row=row, column=1, sticky="ew")
            detail_name.config(state="readonly")

            detail_price = ttk.Entry(frame, width=15)
            detail_price.insert(0, price)
            detail_price.grid(row=row, column=2, sticky="ew")
            detail_price.config(state="readonly")

            detail_imported = ttk.Entry(frame, width=15)
            detail_imported.insert(0, price*quantity)
            detail_imported.grid(row=row, column=3, sticky="ew")
            detail_imported.config(state="readonly")

        def create_void_rows(frame, row):
            products = product.show_products()
            list_products = {}
            for item in products:
                _, p_nombre, p_stock, p_price = item
                list_products[f'{p_nombre}'] = p_price

            option_list = list(list_products.keys())
            option_list.insert(0, "-")

            name_1 = tk.StringVar(frame)
            name_1.set(option_list[0])
            detail_quantity_1 = ttk.Entry(frame, width=30)
            detail_quantity_1.insert(0, '0')
            detail_quantity_1.grid(row=row+1, column=0, sticky="ew")
            detail_name_1 = ttk.OptionMenu(frame, name_1, *option_list, style='vista.TMenubutton')
            detail_name_1.config(width=45)
            detail_name_1.grid(row=row+1, column=1, sticky="ew")
            detail_price_1 = ttk.Entry(frame, width=15)
            detail_price_1.grid(row=row+1, column=2, sticky="ew")
            detail_price_1.config(state="readonly")
            detail_imported_1 = ttk.Entry(frame, width=15)
            detail_imported_1.grid(row=row+1, column=3, sticky="ew")
            detail_imported_1.config(state="readonly")

            name_2 = tk.StringVar(frame)
            name_2.set(option_list[0])
            detail_quantity_2 = ttk.Entry(frame, width=30)
            detail_quantity_2.insert(0, '0')
            detail_quantity_2.grid(row=row+2, column=0, sticky="ew")
            detail_name_2 = ttk.OptionMenu(frame, name_2, *option_list, style='vista.TMenubutton')
            detail_name_2.config(width=45)
            detail_name_2.grid(row=row+2, column=1, sticky="ew")
            detail_price_2 = ttk.Entry(frame, width=15)
            detail_price_2.grid(row=row+2, column=2, sticky="ew")
            detail_price_2.config(state="readonly")
            detail_imported_2 = ttk.Entry(frame, width=15)
            detail_imported_2.grid(row=row+2, column=3, sticky="ew")
            detail_imported_2.config(state="readonly")

            name_3 = tk.StringVar(frame)
            name_3.set(option_list[0])
            detail_quantity_3 = ttk.Entry(frame, width=30)
            detail_quantity_3.insert(0, '0')
            detail_quantity_3.grid(row=row+3, column=0, sticky="ew")
            detail_name_3 = ttk.OptionMenu(frame, name_3, *option_list, style='vista.TMenubutton')
            detail_name_3.config(width=45)
            detail_name_3.grid(row=row+3, column=1, sticky="ew")
            detail_price_3 = ttk.Entry(frame, width=15)
            detail_price_3.grid(row=row+3, column=2, sticky="ew")
            detail_price_3.config(state="readonly")
            detail_imported_3 = ttk.Entry(frame, width=15)
            detail_imported_3.grid(row=row+3, column=3, sticky="ew")
            detail_imported_3.config(state="readonly")

            name_4 = tk.StringVar(frame)
            name_4.set(option_list[0])
            detail_quantity_4 = ttk.Entry(frame, width=30)
            detail_quantity_4.insert(0, '0')
            detail_quantity_4.grid(row=row+4, column=0, sticky="ew")
            detail_name_4 = ttk.OptionMenu(frame, name_4, *option_list, style='vista.TMenubutton')
            detail_name_4.config(width=45)
            detail_name_4.grid(row=row+4, column=1, sticky="ew")
            detail_price_4 = ttk.Entry(frame, width=15)
            detail_price_4.grid(row=row+4, column=2, sticky="ew")
            detail_price_4.config(state="readonly")
            detail_imported_4 = ttk.Entry(frame, width=15)
            detail_imported_4.grid(row=row+4, column=3, sticky="ew")
            detail_imported_4.config(state="readonly")

            name_5 = tk.StringVar(frame)
            name_5.set(option_list[0])
            detail_quantity_5 = ttk.Entry(frame, width=30)
            detail_quantity_5.insert(0, '0')
            detail_quantity_5.grid(row=row+5, column=0, sticky="ew")
            detail_name_5 = ttk.OptionMenu(frame, name_5, *option_list, style='vista.TMenubutton')
            detail_name_5.config(width=45)
            detail_name_5.grid(row=row+5, column=1, sticky="ew")
            detail_price_5 = ttk.Entry(frame, width=15)
            detail_price_5.grid(row=row+5, column=2, sticky="ew")
            detail_price_5.config(state="readonly")
            detail_imported_5 = ttk.Entry(frame, width=15)
            detail_imported_5.grid(row=row+5, column=3, sticky="ew")
            detail_imported_5.config(state="readonly")

            name_6 = tk.StringVar(frame)
            name_6.set(option_list[0])
            detail_quantity_6 = ttk.Entry(frame, width=30)
            detail_quantity_6.insert(0, '0')
            detail_quantity_6.grid(row=row+6, column=0, sticky="ew")
            detail_name_6 = ttk.OptionMenu(frame, name_6, *option_list, style='vista.TMenubutton')
            detail_name_6.config(width=45)
            detail_name_6.grid(row=row+6, column=1, sticky="ew")
            detail_price_6 = ttk.Entry(frame, width=15)
            detail_price_6.grid(row=row+6, column=2, sticky="ew")
            detail_price_6.config(state="readonly")
            detail_imported_6 = ttk.Entry(frame, width=15)
            detail_imported_6.grid(row=row+6, column=3, sticky="ew")
            detail_imported_6.config(state="readonly")

            name_7 = tk.StringVar(frame)
            name_7.set(option_list[0])
            detail_quantity_7 = ttk.Entry(frame, width=30)
            detail_quantity_7.insert(0, '0')
            detail_quantity_7.grid(row=row+7, column=0, sticky="ew")
            detail_name_7 = ttk.OptionMenu(frame, name_7, *option_list, style='vista.TMenubutton')
            detail_name_7.config(width=45)
            detail_name_7.grid(row=row+7, column=1, sticky="ew")
            detail_price_7 = ttk.Entry(frame, width=15)
            detail_price_7.grid(row=row+7, column=2, sticky="ew")
            detail_price_7.config(state="readonly")
            detail_imported_7 = ttk.Entry(frame, width=15)
            detail_imported_7.grid(row=row+7, column=3, sticky="ew")
            detail_imported_7.config(state="readonly")

            name_8 = tk.StringVar(frame)
            name_8.set(option_list[0])
            detail_quantity_8 = ttk.Entry(frame, width=30)
            detail_quantity_8.insert(0, '0')
            detail_quantity_8.grid(row=row+8, column=0, sticky="ew")
            detail_name_8 = ttk.OptionMenu(frame, name_8, *option_list, style='vista.TMenubutton')
            detail_name_8.config(width=45)
            detail_name_8.grid(row=row+8, column=1, sticky="ew")
            detail_price_8 = ttk.Entry(frame, width=15)
            detail_price_8.grid(row=row+8, column=2, sticky="ew")
            detail_price_8.config(state="readonly")
            detail_imported_8 = ttk.Entry(frame, width=15)
            detail_imported_8.grid(row=row+8, column=3, sticky="ew")
            detail_imported_8.config(state="readonly")

            details = [
                [0, detail_quantity_1, name_1, 0],
                [0, detail_quantity_2, name_2, 0],
                [0, detail_quantity_3, name_3, 0],
                [0, detail_quantity_4, name_4, 0],
                [0, detail_quantity_5, name_5, 0],
                [0, detail_quantity_6, name_6, 0],
                [0, detail_quantity_7, name_7, 0],
                [0, detail_quantity_8, name_8, 0],
            ]
            return details

        def save(id, data: dict, details: list[tuple | list] = None):
            print(details)
            if id != 0:
                ticket_details.delete_ticket_details({'boleta_id': id})

            new_data = [{'fecha': data['date'].get(),
                         'nombre': data['name'].get(),
                         'direccion': data['address'].get(),
                         'dni': data['dni'].get()}]

            if id != 0:
                ticket.update_ticket(id, new_data)
            else:
                ticket.new_ticket(new_data)
                # obtener ultimo id

            products = product.show_products()
            list_products = {}
            for item in products:
                p_id, p_nombre, *_ = item
                list_products[f'{p_nombre}'] = p_id
            print(list_products)
            # new_details = [{'boleta_id': ticket_id, 'producto_id': product_id, 'cantidad': quantity},
            #            {'boleta_id': ticket_id, 'producto_id': product_id, 'cantidad': quantity},
            #            ...]
            new_details = []
            if id != 0:
                for item in details:
                    _, quantity, p_name, _ = item
                    new_details.append({'boleta_id': id, 'producto_id': list_products[p_name], 'cantidad': quantity})
                print(new_details)
            else:
                last_id = ticket.show_tickets()[-1][0]
                for item in details:
                    _, quantity, p_name, _ = item
                    if int(quantity.get()) != 0:
                        new_details.append({'boleta_id': last_id, 'producto_id': list_products[p_name.get()], 'cantidad': int(quantity.get())})
                print(new_details)

            ticket_details.new_ticket_details(new_details)

        self.main_frame.destroy()
        self.main_frame = ttk.Frame(self)
        self.main_frame.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')
        self.main_frame.grid_rowconfigure(5, minsize=40)
        self.main_frame.grid_rowconfigure(9, minsize=40)

        # Obtener los datos de la "Empresa"
        _, ruc, c_name, c_address, phone, email = company.show_company()[0]

        # Obtener los datos del ticket si se recibio un id
        if id:
            id, date, name, address, dni = ticket.show_ticket(id)[0]
            details: list[tuple | list] = ticket_details.show_ticket_details(id)
        else:
            id, date, name, address, dni = [0, '', '', '', '']
            date = datetime.today().strftime('%Y-%m-%d')
            details: list[tuple | list] = []

        # ======== Company =============
        company_name = ttk.Label(self.main_frame, text=c_name, width=80,  anchor="center")
        company_name.grid(row=1, column=0, columnspan=2, sticky="w")

        company_address = ttk.Label(self.main_frame, text=c_address, width=80, anchor="center")
        company_address.grid(row=2, column=0, columnspan=2, sticky="w")

        company_phone = ttk.Label(self.main_frame, text=phone, width=80, anchor="center")
        company_phone.grid(row=3, column=0, columnspan=2, sticky="w")

        company_email = ttk.Label(self.main_frame, text=email, width=80, anchor="center")
        company_email.grid(row=4, column=0, columnspan=2, sticky="w")

        company_ruc = ttk.Label(self.main_frame, text=f'ruc: {ruc}', width=30, borderwidth=1, relief="solid", anchor="center")
        company_ruc.grid(row=1, column=2, columnspan=2, sticky="w")

        ticket_type = ttk.Label(self.main_frame, text='Boleta de Venta', width=30, borderwidth=1, relief="solid", anchor="center")
        ticket_type.grid(row=2, column=2, columnspan=2, sticky="w")

        # ======== Ticket =============
        ticket_id = ttk.Label(self.main_frame, text=f'N-{id:0>6}', width=30, borderwidth=1, relief="solid", anchor="center")
        ticket_id.grid(row=3, column=2, columnspan=2, sticky="w")

        ttk.Separator(self.main_frame, orient=tk.HORIZONTAL).grid(row=5, column=0, columnspan=4, sticky="EW")
        ticket_name = ttk.Label(self.main_frame, text='Nombre ')
        ticket_name.grid(row=6, column=0, sticky="w")
        new_name = ttk.Entry(self.main_frame, width=50)
        new_name.insert(0, name)
        new_name.grid(row=6, column=1)

        ticket_address = ttk.Label(self.main_frame, text='Direccion')
        ticket_address.grid(row=7, column=0, sticky="w")
        new_address = ttk.Entry(self.main_frame, width=50)
        new_address.insert(0, address)
        new_address.grid(row=7, column=1,)

        ticket_dni = ttk.Label(self.main_frame, text='Dni')
        ticket_dni.grid(row=8, column=0, sticky="w")
        new_dni = ttk.Entry(self.main_frame, width=50)
        new_dni.insert(0, dni)
        new_dni.grid(row=8, column=1,)

        ticket_date = ttk.Label(self.main_frame, text='Fecha', width=15, borderwidth=1, relief="solid", anchor="center")
        ticket_date.grid(row=6, column=3, sticky="w")
        new_date = ttk.Entry(self.main_frame, width=15)
        new_date.insert(0, date)
        new_date.grid(row=7, column=3, sticky="ew")

        new_data = {'date': new_date, 'name': new_name, 'address': new_address, 'dni': new_dni}

        # ======== Ticket details =============
        details_quantity = ttk.Label(self.main_frame, text='Cantidad', width=30, borderwidth=1, relief="solid", anchor="center")
        details_quantity.grid(row=10, column=0, sticky="w")

        details_name = ttk.Label(self.main_frame, text='Descripcion', width=50, borderwidth=1, relief="solid", anchor="center")
        details_name.grid(row=10, column=1, sticky="w")

        details_price = ttk.Label(self.main_frame, text='Precio', width=15, borderwidth=1, relief="solid", anchor="center")
        details_price.grid(row=10, column=2, sticky="w")

        details_imported = ttk.Label(self.main_frame, text='Importe', width=15, borderwidth=1, relief="solid", anchor="center")
        details_imported.grid(row=10, column=3, sticky="w")

        last_row = 10
        if details:
            print(details)
            for detail in details:
                last_row = last_row + 1
                create_row(self.main_frame, last_row, detail)
        else:
            details = create_void_rows(self.main_frame, last_row)

        button_return = ttk.Button(self.main_frame, text="Descartar", command=self.frame_ticket)
        button_return.grid(row=99, column=0, pady=10, sticky='e')

        button_save = ttk.Button(self.main_frame, text="Guardar", command=lambda: [save(id, new_data, details), self.frame_ticket()])
        button_save.grid(row=99, column=2, pady=10, sticky='w')

    def frame_product(self):
        def delete_product(id):
            product.delete_product({'id': id})

        # Crear el frame para la opción "Productos"
        self.main_frame.destroy()
        self.main_frame = ttk.Frame(self)
        self.main_frame.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

        # Agregar un label al frame de "Productos"
        self.product_label = ttk.Label(self.main_frame, text='Productos')
        self.product_label.grid(row=0, column=0, columnspan=2, pady=10)

        button = ttk.Button(self.main_frame, text="nuevo", command=self.frame_product_template)
        button.grid(row=1, column=0, columnspan=2, pady=10)

        # Obtener productos
        products = product.show_products()

        # last_row = 3
        # for item in products:
        #     last_row = last_row + 1
        #     id, name, stock, price = item
        #     product_summary = ttk.Label(self.main_frame, text=f'{name}\t{stock}\t${price}', width=80, borderwidth=1, relief="solid")
        #     product_summary.grid(row=last_row, column=0, pady=10)
        #     product_edit = ttk.Button(self.main_frame, text='Ver/Editar', command=lambda id=id: self.frame_product_template(id))
        #     product_edit.grid(row=last_row, column=1, pady=10)
        #     product_delete = ttk.Button(self.main_frame, text='Eliminar', command=lambda id=id: [delete_product(id), self.frame_product()])
        #     product_delete.grid(row=last_row, column=2, pady=10)

        # Crear un widget Canvas para contener los productos
        canvas = tk.Canvas(self.main_frame)
        canvas.configure(width=780, height=450)
        canvas.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky='nsew')
        # canvas.bind_all("<MouseWheel>", self.on_mousewheel)

        # Agregar un scrollbar al widget Canvas
        scrollbar = ttk.Scrollbar(self.main_frame, orient='vertical', command=canvas.yview, style="Vertical.TScrollbar")
        scrollbar.grid(row=2, column=2, pady=10, sticky='ns')
        canvas.configure(yscrollcommand=scrollbar.set)

        # Crear un frame dentro del widget Canvas para contener los productos
        products_frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=products_frame, anchor='nw')

        # Agregar los productos al frame dentro del widget Canvas
        last_row = 0
        for item in products:
            id, name, stock, price = item
            product_summary = ttk.Label(products_frame, text=f'{name}\t{stock}\t${price}', width=80, borderwidth=1, relief="solid")
            product_summary.grid(row=last_row, column=0, pady=10)
            product_edit = ttk.Button(products_frame, text='Ver/Editar', command=lambda id=id: self.frame_product_template(id))
            product_edit.grid(row=last_row, column=1, pady=10)
            product_delete = ttk.Button(products_frame, text='Eliminar', command=lambda id=id: [delete_product(id), self.frame_product()])
            product_delete.grid(row=last_row, column=2, pady=10)
            last_row += 1
    def frame_product_template(self, id: int = None):
        def save(id, data):
            name, stock, price = data
            new_data = [{'nombre': name.get(), 'stock': int(stock.get()), 'precio': float(price.get())}]
            print(id, new_data)
            if id != 0:
                product.update_product(id, new_data)
            else:
                product.new_product(new_data)

        if id:
            _, name, stock, price = product.show_product(id)[0]
        else:
            id, name, stock, price = [0, '', '', '']

        self.main_frame.destroy()
        self.main_frame = ttk.Frame(self)
        self.main_frame.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

        product_name = ttk.Label(self.main_frame, text='Nombre')
        product_name.grid(row=1, column=0, padx=30, pady=10, sticky="w")
        new_name = ttk.Entry(self.main_frame, width=40)
        new_name.insert(0, name)
        new_name.grid(row=1, column=1, padx=30, pady=10)

        product_stock = ttk.Label(self.main_frame, text='Stock')
        product_stock.grid(row=2, column=0, padx=30, pady=10, sticky="w")
        new_stock = ttk.Entry(self.main_frame, width=40)
        new_stock.insert(0, stock)
        new_stock.grid(row=2, column=1, padx=30, pady=10)

        product_price = ttk.Label(self.main_frame, text='Precio')
        product_price.grid(row=3, column=0, padx=30, pady=10, sticky="w")
        new_price = ttk.Entry(self.main_frame, width=40)
        new_price.insert(0, price)
        new_price.grid(row=3, column=1, padx=30, pady=10)

        new_data = [new_name, new_stock, new_price]

        button_return = ttk.Button(self.main_frame, text="Descartar", command=self.frame_product)
        button_return.grid(row=99, column=0, pady=10, sticky='e')

        button_save = ttk.Button(self.main_frame, text="Guardar", command=lambda: [save(id, new_data), self.frame_product()])
        button_save.grid(row=99, column=1, pady=10, sticky='e')

    def frame_company(self):
        def update_company(id, ruc, name, address, phone, email):
            ruc = new_ruc.get()
            name = new_name.get()
            address = new_address.get()
            phone = new_phone.get()
            email = new_email.get()
            # print(id,ruc,name,address,phone,email)
            company.update_company(id, ruc, name, address, phone, email)

        # Crear el frame para la opción "Empresa"
        self.main_frame.destroy()
        self.main_frame = ttk.Frame(self)
        self.main_frame.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

        # Agregar un label al frame de "Empresa"
        self.company_label = ttk.Label(self.main_frame, text='Empresa')
        self.company_label.grid(row=0, column=0, columnspan=2, pady=10, sticky='n')

        # Obtener los datos de la "Empresa"
        id, ruc, name, address, phone, email = company.show_company()[0]

        company_ruc = ttk.Label(self.main_frame, text='Ruc')
        company_ruc.grid(row=1, column=0, padx=30, pady=10, sticky="w")
        new_ruc = ttk.Entry(self.main_frame, width=40)
        new_ruc.insert(0, ruc)
        new_ruc.grid(row=1, column=1, padx=30, pady=10)

        company_name = ttk.Label(self.main_frame, text='Nombre')
        company_name.grid(row=2, column=0, padx=30, pady=10, sticky="w")
        new_name = ttk.Entry(self.main_frame, width=40)
        new_name.insert(0, name)
        new_name.grid(row=2, column=1, padx=30, pady=10)

        company_address = ttk.Label(self.main_frame, text='Direccion')
        company_address.grid(row=3, column=0, padx=30, pady=10, sticky="w")
        new_address = ttk.Entry(self.main_frame, width=40)
        new_address.insert(0, address)
        new_address.grid(row=3, column=1, padx=30, pady=10)

        company_phone = ttk.Label(self.main_frame, text='Celular')
        company_phone.grid(row=4, column=0, padx=30, pady=10, sticky="w")
        new_phone = ttk.Entry(self.main_frame, width=40)
        new_phone.insert(0, phone)
        new_phone.grid(row=4, column=1, padx=30, pady=10)

        company_email = ttk.Label(self.main_frame, text='E-mail')
        company_email.grid(row=5, column=0, padx=30, pady=10, sticky="w")
        new_email = ttk.Entry(self.main_frame, width=40)
        new_email.insert(0, email)
        new_email.grid(row=5, column=1, padx=30, pady=10)

        button = ttk.Button(self.main_frame, text="Guardar", command=lambda: update_company(id, new_ruc, new_name, new_address, new_phone, new_email))
        button.grid(row=6, column=0, columnspan=2, pady=10)

    def salir(self):
        self.quit()


if __name__ == '__main__':
    ticket = Ticket()
    product = Product()
    company = Company()
    ticket_details = TicketDetails()
    app = App()
    app.mainloop()
