from restaurant import Restaurant


def main():
    print("Wellcome to ")
    name = input("please ")
    address = input("please ")
    phone_number = input("please ")
    description = input("please ")
    restaurant = Restaurant(name, address, phone_number, description)
    management_system = restaurant.create_management_system()


