from reservation import Reservation
from order import Order


class Table:
    table_id = 0

    def __init__(self, max_capacity):
        Table.table_id += 1
        self.__tableID = Table.table_id
        self.__table_status = False
        self.__max_capacity = max_capacity
        self.__reservation_id = 0

    def add_reservation(self, reservation):
        if not self.tabel_status and self.max_capacity / 2 <= reservation.number_of_people <= self.__max_capacity:
            self.__reservation_id = reservation.reservation_id
            self.__table_status = True
            return True
        return False

    def create_order(self,customer):
        new_order = Order(self.table_id, customer.id)
        return new_order

    def free_table(self):
        self.__table_status = False


    @property
    def tableID(self):
        return self.__tableID

    @tableID.setter
    def tableID(self, tableID):
        self.__tableID = tableID

    @property
    def table_status(self):
        return self.__table_status

    @table_status.setter
    def table_status(self, table_status):
        self.__table_status = table_status

    @property
    def max_capacity(self):
        return self.__max_capacity

    @max_capacity.setter
    def name(self, max_capacity):
        self.__max_capacity = max_capacity