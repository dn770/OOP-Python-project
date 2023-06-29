def ongoing_loop(management_system):
    while True:
        option = int(input("to reservation insert 1,\
         to shipping insert 2, to take order insert 3 ,\
          \
          to shut down insert 0\n"))
        if not option:
            return
        elif option == 1:
            reserv = management_system.create_reservation(input("Time: "), input(" num of people: "))
            management_system.tables[0].add_reservation(reserv)
        elif option == 2:
            ships = management_system.create_shipping(input("Address: "))
            ships.create_order()
        elif option == 3:
            management_system.create_take_order(input("order_id: "))
