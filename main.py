import project

dict_item = {}
print("\n..........Welcome!..........")

while True:
    try:
        print("\nMAIN MENU")
        print("---------")
        print("1. Input item \n2. Update item \n3. Delete item \n4. Check order \n5. Checkout your order\n6. Exit\n")
        menu = int(input("What would you like to do? (input a number based on the menu above): ").strip())
        print("----------------------------------------------------------------------")
        if menu == 1:
            dict_item = project.input_item()
        elif menu == 2:
            if dict_item == {}:
                print("\nThere's no item to be updated")
            else: 
                project.check_order()
                print("")
                dict_item = project.update_item()
        elif menu == 3:
            if dict_item == {}:
                print("\nThere's no item to be deleted")
            else: dict_item = project.delete_item()
        elif menu == 4:
            if dict_item == {}:
                print("\nThere's no order yet!")
            else: project.check_order()
        elif menu == 5: 
            if dict_item == {}:
                print("\nThere's no order yet!")
            else: 
                project.check_order()
                print("")
                project.total_price()
                print("\nThank you for coming!\n")
                break
        elif menu == 6:
            print("\nThank you for coming!\n")
            break 
    except:
        print("\nPlease only input number based on the menu above")