def ongoing_loop(management_system):
    while True:
        option = int(input("to reservation insert 1,\
         to shipping insert 2, to take order insert 3 ,\
          \
          to shut down insert 0\n"))
        if not option:
            return
        elif option == 1:
            management_system.create_reservation()
        elif option == 2:
            management_system.create_shipping()
        elif option == 3:
            management_system.create_take_order()
