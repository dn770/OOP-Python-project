class Bill:
    def __int__(self, billID,customerID, payment_type):
        self.__billID = billID
        self.__customerID = customerID
        self.__payment_type = payment_type

    def pay(self):
        pass

    def cancel_payment(self):
        pass

    @property
    def billID(self):
        return self.__billID

    @billID.setter
    def billID(self,billID):
        self.__billID = billID

    @property
    def customerID(self):
        return self.__customerID

    @customerID.setter
    def order_status(self, customerID):
        self.__customerID = customerID

    @property
    def payment_type(self):
        return self.__payment_type

    @payment_type.setter
    def payment_type(self, payment_type):
        self.__payment_type = payment_type

