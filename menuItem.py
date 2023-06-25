class MenuItem:
    menu_item_id = 0

    def __init__(self, title, description, price):
        MenuItem.menu_item_id += 1
        self.__menuItemID = MenuItem.menu_item_id
        self.__title = title
        self.__description = description
        self.__price = price

    def update_price(self,price):
        self.price = price

    @property
    def menuItemID(self):
        return self.__menuItemID

    @menuItemID.setter
    def menuItemID(self,menuItemID):
        self.__menuItemID = menuItemID

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, payment_type):
        self.__description = description

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price