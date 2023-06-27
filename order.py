from customer import Customer
from managment_system import ManagementSystem
from table import Table
from bill import Bill
class Order:
    order_id = 0

    def __int__(self,table_id, customer_id, payment_type):
        Order.order_id += 1
        self.__orderID = Order.order_id
        self.__order_status = False
        self.__order_items = []
        self.__order_price = 0
        self.__table_id = table_id
        self.__customer_id = customer_id
        self.__bill = Bill(payment_type)

    def calculate_price(self):
        p_sum = 0
        for item in self.__order_items:
            p_sum += item.price
        self.__order_price = p_sum

    def add_menu_item(self, menu_id, menu_item_id):
        for menu in ManagementSystem.menus:
            if menu.menu_id == menu_id:
                for item in menu:
                    if item.menu_item_id == menu_item_id:
                        self.__order_items.append(item)
                        break
                break

        self.calculate_price()

    def remove_menu_item(self, menu_item_id):
        for item in self.__order_items:
            if item.menu_item_id == menu_item_id:
                self.__order_items.remove(item)
                break
        self.calculate_price()

    def end_order(self):
        if self.__order_status and self.__bill.payment_status:
            ManagementSystem.remove_order(self.order_id)
            Table.free_table(self.table_id)
            Customer.check_out(self.__customer_id)

    @property
    def orderID(self):
        return self.__orderID

    @orderID.setter
    def orderID(self, orderID):
        self.__orderID = orderID

    @property
    def order_status(self):
        return self.__order_status

    @order_status.setter
    def order_status(self, order_status):
        self.__order_status = order_status
