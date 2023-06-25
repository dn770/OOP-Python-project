class Shipping:

    shipping_id = 0

    def __init__(self, shipping_address):
        Shipping.shipping_id =+ 1
        self.__shipping_id = Shipping.shipping_id
        self.__shipping_address = shipping_address

    def change_adress(self, shipping_address):
        self.shipping_address = shipping_address

        @property
        def shipping_id(self):
            return self.__shipping_id

        @shipping_id.setter
        def shipping_id(self, shipping_id):
            self.__shipping_id = shipping_id

        @property
        def shipping_address(self):
            return self.__shipping_address

        @tables.setter
        def ashipping_address(self, shipping_address):
            self.__shipping_address = shipping_address