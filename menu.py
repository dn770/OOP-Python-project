import menuItem


class Menu:
    menu_id = 0

    def __init__(self):
        Menu.menu_id += 1
        self.__menu_id = Menu.menu_id
        self.__items = []

    def add_menu_item(self, menu_item):
        self.__items.append(menu_item)

    def remove_menu_item(self,menu_item_id):
        for item in self.__items:
            if item.menu_item_id == menu_item_id:
                self.__items.remove(item)
                break

    def clear_menu(self):
        self.__items.clear()

    @property
    def menu_id(self):
        return self.__menuID

    @menu_id.setter
    def menu_id(self, menu_id):
        self.__menu_id = menu_id

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, items):
        self.__items = items
