class Table:
    table_id = 0
    def __init__(self, max_capacity):
        Table.table_id += 1
        self.__tableID = Table.table_id
        self.__table_status = False
        self.__max_capacity = max_capacity
        self.__reservation_id = 0

    def add_reservation(self, reservation_id):
        self.__reservation_id = reservation_id
        self.__table_status = True

    def create_order(self):
        pass

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