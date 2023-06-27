class Order:
    order_id = 0
    def __int__(self,table_id, customer_id):
        Order.order_id += 1
        self.__orderID = Order.order_id
        self.__order_status = False
        self.__order_items = []
        self.__order_price = sum(self.__order_items.menu_item.price)
        self.__table_id = table_id
        self.__customer_id = customer_id

    def add_menu_item(self, menu_item):
        self.__order_items.append(menu_item)

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
