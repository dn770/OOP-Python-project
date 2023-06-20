class Customer:
    def __int__(self, name, customerID, contact_number):
        self.__name = name
        self.__customerID = customerID
        self.__contact_number = contact_number

    def chack_in(self):
        pass

    def chack_out(self):
        pass
    def modify_order(self):
        pass

    def cancel_order(self):
        pass

    def last_visited(self):
        pass

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def customerID(self):
        return self.__name

    @customerID.setter
    def customerID(self, customerID):
        self.__customerID = customerID

    @property
    def contact_number(self):
        return self.__contact_number

    @contact_number.setter
    def name(self, contact_number):
        self.__contact_number = contact_number