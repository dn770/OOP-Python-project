import menuItem
class Menu:
    menuID = 0

    def __init__(self):
        Menu.menuID += 1
        self.__menuID = Menu.menuID
        self.__items = []

    def add_menuItem(self, menuItem):
        self.__items.append(menuItem)

    def remove_menuItem(self,menuItemID):
        for item in self.__items:
            if item.menuItemID == menuItemID:
                self.__items.remove(item)
                break

    def clear_menu(self):
        self.__items.clear()

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
    def items(self,items):
        self.__items = items