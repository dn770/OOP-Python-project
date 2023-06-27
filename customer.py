
class Customer:
    customer_id = 0

    def __init__(self, name, contact_number):
        Customer.customer_id += 1
        self.__name = name
        self.__customer_id = Customer.customer_id
        self.__contact_number = contact_number
        self.__customer_mode = True

    def check_in(self):
        self.__customer_mode = True

    def check_out(self):
        self.__customer_mode = False


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def customer_id(self):
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        self.__customer_id = customer_id

    @property
    def contact_number(self):
        return self.__contact_number

    @contact_number.setter
    def contact_number(self, contact_number):
        self.__contact_number = contact_number
