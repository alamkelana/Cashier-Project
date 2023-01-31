from store import input_item, update_item, delete_item, check_order, total_price
from color_func import printGreen, printRed, printYellow

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
            dict_item = input_item()
        elif menu == 2:
            if dict_item == {}:
                printRed("\nThere's no item to be updated")
            else: 
                check_order()
                print("")
                dict_item = update_item()
        elif menu == 3:
            if dict_item == {}:
                printRed("\nThere's no item to be deleted")
            else: dict_item = delete_item()
        elif menu == 4:
            if dict_item == {}:
                printRed("\nThere's no order yet!")
            else: check_order()
        elif menu == 5: 
            if dict_item == {}:
                printRed("\nThere's no order yet!")
            else: 
                check_order()
                total_price()
                printGreen("\nThank you for coming!\n")
                break
        elif menu == 6:
            printGreen("\nThank you for coming!\n")
            break 
    except:
        printRed("\nPlease only input number based on the menu above")