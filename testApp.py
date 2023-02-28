from Ticket import Ticket
from Product import Product
from Company import Company
from TicketDetails import TicketDetails


ticket = Ticket()
product = Product()
company = Company()
ticket_details = TicketDetails()

while True:
    print("1-new_ticket")
    print("2-update_ticket")
    print("3-show_tickets")
    print("4-delete_ticket")
    print("5-new_product")
    print("6-update_product")
    print("7-show_product")
    print("8-delete_product")
    print("9-update_company")
    print("10-show_company")
    print("11-view_ticket_details")
    print("12-delete_ticket_details")
    print("0-exit")

    option = int(input(">>> "))

    match option:
        case 1:
            ticket.new_ticket()
            ticket_details.new_ticket_details()
        case 2:
            ticket.update_ticket()
            ticket_details.update_ticket_details()
        case 3:
            ticket.show_tickets()
        case 4:
            ticket.delete_ticket()
        case 5:
            product.new_product()
        case 6:
            product.update_product()
        case 7:
            product.show_products()
        case 8:
            product.delete_product()
        case 9:
            company.update_company()
        case 10:
            company.show_company()
        case 11:
            ticket_details.show_ticket_details()
        case 12:
            ticket_details.delete_ticket_details()
        case 0:
            break
