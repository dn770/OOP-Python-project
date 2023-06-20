class Menu:
    def __int__(self, menuID, items):
        self.__menuID = menuID
        self.__items = items

    def add_menuItem(self, menuItem):
        items.append(menuItem)

    @property
    def menuID(self):
        return self.__menuID

    @menuID.setter
    def menuID(self,menuID):
        self.__menuID = menuID

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, items):
        self.__items = items

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
        self.