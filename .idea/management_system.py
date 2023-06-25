import restaurant
class ManagementSystem:

    def __init__(self):
        self.__menus = []
        self.__tables = []

    def add_menu(self,menu):
        self.__menus.append(menu)

    def add_table(self,table):
        self.__tables.append(table)

    def take_order(self,order):
        order.order_status = True

    def create_resevation(self):
        Reservision(time, num_of_people)

    def create_shipping(self):
        Shipping(adress)

