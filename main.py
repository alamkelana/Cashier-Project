"""
This is the main program, it has the main menu, and the if function to run the function
inside store.py based on user selection
You have to run color_func.py and store.py before you run this main.py
"""

#Import the functions from store.py
from store import input_item, update_item, delete_item, check_order, total_price, show_cart

#Import color_func.py to print in color
from color_func import printGreen, printRed

#Declare the dict_item dictionary as empty dictionary so it can be filled and modified later
dict_item = {}

print("\n..........Welcome!..........")

#Use infinite loop so that whichever function we ran, we are going back to main menu
while True:
    try:

        #Print the main menu
        print("\nMAIN MENU")
        print("---------")
        print("1. Input item \n2. Update item \n3. Delete item \n4. Check order \n5. Checkout your order\n6. Exit\n")
        menu = int(input("What would you like to do? (input a number based on the menu above): ").strip())
        print("----------------------------------------------------------------------")
        
        #Main if, running the functions from store.py based on the user input
        if menu == 1:
            dict_item = input_item()

        elif menu == 2:

            #Checking whether the item already inputted or not
            if dict_item == {}:
                printRed("\nThere's no item to be updated")

            #If the item already inputted, we run the function update_item 
            else: 

                #Showing the check_order first so the user can remember the item(s) they have inputted
                show_cart()
                print("")
                dict_item = update_item()

        elif menu == 3:

            #Checking whether the item already inputted or not
            if dict_item == {}:
                printRed("\nThere's no item to be deleted")

            #If the item already inputted, we run the function delete_item
            else: 

                #Showing the check_order first so the user can remember the item(s) they have inputted
                show_cart()
                print("")
                dict_item = delete_item()

        elif menu == 4:

            #Checking whether the item already inputted or not
            if dict_item == {}:
                printRed("\nThere's no order yet!")

            #If the item already inputted, we run the function check_order
            else: check_order()

        elif menu == 5: 

            #Checking whether the item already inputted or not
            if dict_item == {}:
                printRed("\nThere's no order yet!")

            #If the item already inputted, we run the function total_price
            else: 

                #Showing the check_order first to show all the item(s) the user inputted before
                check_order()
                total_price()
                printGreen("\nThank you for coming!\n")
                
                #Break the infinite loop when you check out the order
                break

        elif menu == 6:

            #Break from the infinite loop if the user want to exit the program before they check out
            printGreen("\nThank you for coming!\n")
            break 

    #Giving error message if the user input is not 1,2,3,4,5, or 6
    except:
        printRed("\nPlease only input number based on the menu above")