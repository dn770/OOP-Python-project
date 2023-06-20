class Table:
    def __int__(self, tableID, table_status, max_capacity):
        self.__tableID = tableID
        self.__table_status = table_status
        self.__max_capacity = max_capacity

    def addReservation(self):
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