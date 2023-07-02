def ongoing_loop(management_system):
    while True:
        option = input(" insert 1 - to add reservation\n\
          2- to add shipping\n,3 - to take order\n \
          4 - to bill\n 5- to update menus\n 6 - to update menuItems\n 7- to update customers\n \
          8 - to update tables\n 9- to   0 - to exit\n")
        if not option: # 0 -> exit
            return
        elif option == "1" or "2": # create reservation
            if option == "1":
                reserv = management_system.create_reservation(input("Time: "), input("num of people: "))
                table = management_system.match_table(reserv)
            else:# option = 2
                ships = management_system.create_shipping(input("Address: "))
                table = 0
            #create order acorrding the reservation or shipping details
            ans = input("New customer or old customer ? n/o")
            if ans == "n":



            management_system.create_order(table, customer, payment_type)

            ships.create_order()
        elif option == "3": # take order
            management_system.create_take_order(input("order_id: "))
        elif option == "4": # bill
            sub_option = input("")
        elif option == "5": # update menus
                sub_option = input(" insert 1 - to add new menu\n 2 - to remove menu\n 3 - to clear menu\n")
                if sub_option == "1":
                    management_system.add_menu(input("type: "))
                elif sub_option == "2":
                    management_system.remove_menu(input("menu_id = "))
                elif sub_option == "3":
                    management_system.clear_menu(input("menu_id = "))
                else:
                    print("invalid option, back to main-menu")
        elif option == "6": # update menuItems
            sub_option = input(" insert 1 - to add new menu\n 2 - to remove menu\n 3 - to clear menu\n")
            if sub_option == "1":
                management_system.add_menu(input("type: "))
            elif sub_option == "2":
                management_system.remove_menu(input("menu_id = "))
        elif option == "7": # update customers
            sub_option = input(" insert 1 - to add new customer \n 2 - to remove customer\n")
            if sub_option == "1":
                management_system.add_customer(input("name: "), input("contact_number: "))
            elif sub_option == "2":
                management_system.remove_customer(input("customer_id = "))
        elif option == "8": # update tables
            sub_option = input(" insert 1 - to add new table\n 2 - to remove table\n")
            if sub_option == "1":
                management_system.add_table(input("capacity: "))
            elif sub_option == "2":
                management_system.remove_table(input("table_id = "))
        elif option == "9":
            continue
