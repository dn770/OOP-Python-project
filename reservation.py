class Reservation:
    reservation_count = 0

    def __init__(self, reservation_time, number_of_people):
        Reservation.reservation_count += 1
        self.__reservation_id = Reservation.reservation_count
        self.__reservation_time = reservation_time
        self.__number_of_people = number_of_people

    def change_reservation_time(self, reservation_time):
        self.__reservation_time = reservation_time

    @property
    def reservation_id(self):
        return self.__reservation_id

    @reservation_id.setter
    def reservation_id(self, reservation_id):
        self.__reservation_id = reservation_id

    @property
    def reservation_time(self):
        return self.__reservation_time

    @reservation_time.setter
    def reservation_time(self, reservation_time):
        self.__reservation_time = reservation_time

    @property
    def number_of_people(self):
        return self.__number_of_people

    @number_of_people.setter
    def name(self, number_of_people):
        self.__number_of_people = number_of_people
