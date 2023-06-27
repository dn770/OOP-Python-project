from customer import Customer
from order import Order
from management_system import ManagementSystem

class Shipping:

    shipping_id = 0

    def __init__(self, shipping_address):
        Shipping.shipping_id =+ 1
        self.__shipping_id = Shipping.shipping_id
        self.__shipping_address = shipping_address
        self.__order_id = 0

    def change_address(self, shipping_address):
        self.shipping_address = shipping_address

    def create_order(self, customer):
        new_order = Order(0, customer.customer_id) # table = 0 - no table
        self.order_id = new_order.order_id
        ManagementSystem.orders.append(new_order)
        return new_order


    @property
    def shipping_id(self):
        return self.__shipping_id

    @shipping_id.setter
    def shipping_id(self, shipping_id):
        self.__shipping_id = shipping_id

    @property
    def shipping_address(self):
        return self.__shipping_address

    @shipping_address.setter
    def shipping_address(self, shipping_address):
        self.__shipping_address = shipping_address

    @property
    def order_id(self):
        return self.__order_id

    @order_id.setter
    def shipping_address(self, order_id):
        self.__order_id = order_id
