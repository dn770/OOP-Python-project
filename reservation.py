class Reservation:
    def __int__(self, reservationID, reservation_time, number_of_people):
        self.__reservationID = reservationID
        self.__reservation_time = reservation_time
        self.__number_of_people = number_of_people

    def cancel_reservation(self):
        pass

    def change_reservation_time(self):
        pass

    @property
    def reservationID(self):
        return self.__reservationID

    @reservationID.setter
    def reservationID(self, reservationID):
        self.__reservationID = reservationID

    @property
    def reservation_time(self):
        return self.__reservation_time

    @reservation_time.setter
    def customerID(self, reservation_time):
        self.__reservation_time = reservation_time

    @property
    def contact_number(self):
        return self.__contact_number

    @number_of_people.setter
    def name(self, number_of_people):
        self.__number_of_people = number_of_people