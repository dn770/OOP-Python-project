class Order:
    def __int__(self, orderID, order_status):
        self.__orderID = orderID
        self.__order_status = order_status

    def add_menu_item(self):
        pass

    def remove_menu_item(self):
        pass

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
