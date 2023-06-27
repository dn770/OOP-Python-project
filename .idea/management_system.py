from restaurant import Restaurant
from menu import Menu
from table import Table
from order import Order
from shipping import Shipping
from customer import Customer

class ManagementSystem():

    def __init__(self):
        self.__menus = []
        self.__tables = []
        self.__customer = []

    def add_menu(self):
        menu = Menu()
        self.__menus.append(menu)

    def remove_menu(self, menu_id):
        for menu in menus:
            if menu.menu_id == menus.id:
                menus.remove(menu)

    def add_table(self,max_capacity):
        table = Table(max_capacity)
        self.__tables.append(table)

    def ramove_table(self, table_id):
        for table in tables:
            if table.table_id == table.id:
                tables.remove(table)

    def add_customer(self, name, contant_number):
        customer = Customer(name, contant_number)
        self.__customers.append(customer)

    def remove_customer(self, customer_id):
        for customer in customers:
            if customer.customer_id == customer.id:
                customer.remove(customer)

    def take_order(self,Order):
        order.order_status = True

    def create_resevation(self, time, num_of_people):
        reservation = Reservision(time, num_of_people)
        return reservation

    def create_shipping(self):
        shipping = Shipping(adress)
        return shipping

    @property
    def menus(self):
        return self.__menus

    @menus.setter
    def menus(self,menus):
        self.__menus = manues

    @property
    def tables(self):
        return self.__tables

    @tables.setter
    def tables(self, tables):
        self.__tables = tables

    @property
    def customers(self):
        return self.__customers

    @customers.setter
    def customers(self, customers):
        self.__customers = customers