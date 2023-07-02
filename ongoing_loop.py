def ongoing_loop(management_system):
    while True:
        option = input(" insert 1 - to add reservation\n\
          2- to add shipping\n,3 - to take order\n \
          4 - to bill\n 5- to update menus\n 6 - to update menuItems\n 7- to update customers\n \
          8 - to update tables\n 9- to show data \n   0 - to exit\n")
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
                customer = management_system.add_customer(input("name: "), input("contact_number: "))
                customer.check_in()
            else:
                for cust in management_system.customers:
                    if cust.contact_number == input("contact_number: "):
                        cust.check_in()
                        customer = cust
                        break

            management_system.create_order(table, customer, input("payment_type: "))

            #update address of shipping
            if option == "2":
                ans = "Are you want to change the address? y/n\n"
                if ans == 'y':
                    ships.change_adress(input("new address: "))

        elif option == "3": # take order to the kitchen
            management_system.take_order() # find the first order in the list that satus is false

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
            sub_option = input(" insert 1 - to add new menuItem\n 2 - to remove menuItem\n 3 - to update price of menuItem")
            menu_id = input("choose menu by id: ")
            for menu in management_system.menus:
                if menu.menu_id == menu_id:
                    if sub_option == "1":
                        management_system.menu.add_menuitem(input("title: "),input("description: "), float(input("price: ")))
                    elif sub_option == "2":
                        management_system.remove_menu(input("menuItem_id: "))
                    elif sub_option == "3":
                        item_id = input("menuItem_id: ")
                        for item in menu.items:
                            if item.menu_item_id == item_id:
                                item.price = float(input("new price: "))
                    break


        elif option == "7": # update customers
            sub_option = input(" insert 1 - to add new customer \n 2 - to remove customer\n 3- update contact_number\n")
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
            print()
            continue
