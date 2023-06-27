from management_system import ManagementSystem


class Restaurant:

    def __init__(self, name, address, phone_number, description):
        self.__name = name
        self.__address = address
        self.__phone_number = phone_number
        self.__description = description

    def create_management_system(self):
        return ManagementSystem()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def price(self, phone_number):
        self.__phone_number = phone_number
