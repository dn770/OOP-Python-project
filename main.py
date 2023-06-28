from restaurant import Restaurant


def main():
    print("Wellcome to ")
    name = input("please ")
    address = input("please ")
    phone_number = input("please ")
    description = input("please ")
    restaurant = Restaurant(name, address, phone_number, description)
    management_system = restaurant.create_management_system()
    for num in range(int(input("please"))):
        cap = int(input("insert capacity of table ",num))
        management_system.add_table(cap)
    for num in range(int(input("please"))):
        int(input("insert  of menu ",num))
        management_system.add_menu()



main()