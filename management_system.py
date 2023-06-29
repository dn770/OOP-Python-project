from menu import Menu
from customer import Customer
from reservation import Reservation
from table import Table
from shipping import Shipping


class ManagementSystem:

    def __init__(self):
        self.__menus = []
        self.__tables = []
        self.__customer = []
        self.__reservations = []
        self.__orders = []

    def add_menu(self):
        menu = Menu()
        self.__menus.append(menu)

    def remove_menu(self, menu_id):
        for menu in self.menus:
            if menu.menu_id == menu_id:
                self.menus.remove(menu)

    def add_table(self,max_capacity):
        table = Table(max_capacity)
        self.__tables.append(table)

    def remove_table(self, table_id):
        for table in self.tables:
            if table.table_id == table.id:
                self.tables.remove(table)

    def add_customer(self, name, contant_number):
        customer = Customer(name, contant_number)
        self.__customers.append(customer)

    def remove_customer(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer.id:
                customer.remove(customer)

    def take_order(self, order_id):
        for order in self.orders:
            if order.order_status == order_id:
                order.status = True

    def create_reservation(self, time, num_of_people):
        reservation = Reservation(time, num_of_people)
        self.reservations.append(reservation)
        return reservation

    def create_shipping(self,address):
        shipping = Shipping(address)
        return shipping

    @property
    def menus(self):
        return self.__menus

    @menus.setter
    def menus(self,menus):
        self.__menus = menus

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

    @property
    def orders(self):
        return self.__orders

    @orders.setter
    def orders(self, orders):
        self.__orders = orders

    @property
    def reservations(self):
        return self.__reservations

    @reservations.setter
    def reservations(self, reservations):
        self.__reservations = reservations
