"""
This file contains functions that is required to run the main.py file
it consists of functions to modify the main dictionary "dict_item" that will be modified based on the command  
You have to run this file before running main.py
"""

#Import tabulate library to print table using tabulate format
from tabulate import tabulate

#Import color_func.py to print in color
from color_func import printGreen, printRed, printYellow

# fungsi buat ID transaksi

#Declare the dict_item dictionary as empty dictionary so it can be filled and modified later
dict_item = {}

#Function 1: input_item
def input_item():
    """
    This function is used to input new item into empty or filled dict_item dictionary
    The desired input for the dictionary is:
    string for item_name, integer for total item, and integer for item_price
    """

    #Declare dict_item as global variables so it can be modified inside all functions
    global dict_item

    try:
        #Use infinite loop so it can input different file numerous times
        while True:
            nama_item = input("Input item name: ").strip().title()
            jumlah_item = int(input("Input total item: ").strip())
            harga_item = int(input("Input item price: ").strip())

            #Use if function so that the item with same name can't be inputted twice
            if nama_item in dict_item:
                printRed("\nError! Item already in your order")
            else:
                #If item name hasn't been inputted before, input the item details into dict_item
                dict_item[nama_item] = [jumlah_item, harga_item]
            print("----------------------------------------------------------------------")

            #Use infinite loop to ask if the user want to input another item
            #If the input is not Y/N, it will keep asking the user to input Y/N
            while True:
                yn = input("Input another?? (Y/N): ").strip().lower()
                if yn == "y":
                    break

                elif yn == "n":
                    print("----------------------------------------------------------------------")
                    printGreen("The item(s) was added successfully")
                    print("----------------------------------------------------------------------")
                    return
                else:

                    printRed("\nPlease input Y/N only")
                    continue

        print("----------------------------------------------------------------------")
        printGreen("The item(s) was added successfully")
        print("----------------------------------------------------------------------")

        #Return dict_item dictionary from the function as output
        return dict_item

    #Giving error message if the user input non integer into 'total item' and 'item price'
    except:
        printRed("\nPlease only input number to 'total item' and 'item price'")


#Function 2: update_item
def update_item():
    """
    This function is used to make the user choose the kind of update that they want,
    and update the item based on the user input
    """

    #Declare dict_item as global variables so it can be modified inside all functions
    global dict_item

    #Make a menu to choose different type of updates
    print("1. Update item name \n2. Update total item \n3. Update item price ")
    update = int(input("Choose update type (input a number based on the menu above): ").strip())

    #Use if for the number that the user choose, so it will update based on user selection from update menu
    #If the user choose 1, we will update the item name
    if update == 1:

        #Ask user which item they'd like to update
        update_item = input("Input item name that you'd like to update: ").strip().title()

        #Make sure that the item is already inputted, if not, it will run an error message
        if update_item in dict_item.keys():
            updated_item = input("Input new item name: ").strip().title()

            #Update the dictionary keys
            dict_item[updated_item] = dict_item[update_item]

            #Delete the old dictionary keys
            del dict_item[update_item]
            print("----------------------------------------------------------------------")
            printGreen("The item name was updated successfully")
            print("----------------------------------------------------------------------")

        #Print error message if the item is not present in the dictionary
        else: 
            printRed(f"\nNo present item with name {update_item}")

    #If the user choose 2, we will update the total item
    elif update == 2:

        #Ask user which item they'd like to update 
        update_jumlah = input("Input item name that you'd like to update: ").strip().title()

        #Make sure that the item is already inputted, if not, it will run an error message
        if update_jumlah in dict_item.keys():
            updated_jumlah = int(input("Input new total item: ").strip())

            #Update total item
            dict_item[update_jumlah][0] = updated_jumlah
            print("----------------------------------------------------------------------")
            printGreen("Total item was updated successfully")
            print("----------------------------------------------------------------------")

        #Print error message if the item is not present in the dictionary
        else: printRed(f"\nNo present item with name {update_jumlah}")

    #If the user choose 3, we will update the item price
    elif update == 3:

        #Ask user which item they'd like to update
        update_harga = input("Input item name that you'd like to update: ").strip().title()

        #Make sure that the item is already inputted, if not, it will run an error message
        if update_harga in dict_item.keys():
            updated_harga = int(input("Input new item price: ").strip())

            #Update item price
            dict_item[update_harga][1] = updated_harga
            print("----------------------------------------------------------------------")
            printGreen("The item price was updated successfully")
            print("----------------------------------------------------------------------")

         #Print error message if the item is not present in the dictionary
        else: printRed(f"\nNo present item with name {update_harga}")
    
    #Print error message if the user input is not 1,2, or 3
    else: printRed("\nPlease only input number based on the menu above")

    #Return dict_item dictionary from the function as output
    return dict_item

#Function 3: delete_item
def delete_item():
    """
    This function is used to make the user choose between deleting certain item or reset all transaction,
    then delete the item(s) based on the user input
    """

    #Declare dict_item as global variables so it can be modified inside all functions
    global dict_item

    #Make a menu to choose different type of deletes
    print("1. Delete an item \n2. Reset all transaction")
    delete = int(input("Choose delete type (input a number based on the menu above): ").strip())

    #Use if for the number that the user choose, so it will update based on user selection from update menu
    #If the user choose 1, we will delete a certain item
    if delete == 1:

        #Ask user which item they'd like to delete 
        item_delete = input("Input item name: ").strip().title()

        #Make sure that the item is already inputted, if not, it will run an error message
        if item_delete in dict_item.keys():

            #Delete the item and its details
            del dict_item[item_delete]
            print("----------------------------------------------------------------------")
            printGreen("The item was deleted successfully")
            print("----------------------------------------------------------------------")
        
         #Print error message if the item is not present in the dictionary
        else: printRed(f"No present item with name {item_delete}")

    #If the user choose 2, we will reset the transaction and make the dict_item dictionary empty
    elif delete == 2:

        #Make the dict_item dictionary empty
        dict_item = {}
        print("----------------------------------------------------------------------")
        printGreen("All items was deleted successfully")
        print("----------------------------------------------------------------------")

    #Print error message if the user input is not 1 or 2
    else: printRed("\nPlease only input number based on the menu above")

    #Return dict_item dictionary from the function as output
    return dict_item


#Funtion 4: check_order
def check_order():
    """This function is used to show the total order that the user inputted
    using tabulate library
    """

    #Adjusting the dictionary using list comprehension so it will fit the tabulate input format
    print_dict = {"Item Name" : [i for i in dict_item.keys()],
            "Total Item": [i[0] for i in dict_item.values()],
            "Price": [i[1] for i in dict_item.values()],
            "Total": [i[0]*i[1] for i in dict_item.values()]}

    #Printing the table of inputted order using tabulate
    printGreen("\nOrder Details: \n")
    print(tabulate(print_dict, headers = "keys", tablefmt = "github"))
    print("----------------------------------------------------------------------")

#Function 5: total_price
def total_price():
    """
    This function is used to count the total of money the user have to pay,
    count the discount based on different conditions, count the discounted price
    and show the user all these informations
    
    Dscount condition:
    -5% discount for total order above Rp 200000
    -8% discount fot total order above Rp 300000
    -10% discount for total order above Rp 500000"""

    #Using for and updating 'total' variable to sum the total price the user have to pay
    total = 0
    for key in dict_item.keys():
        total = total+(dict_item[key][0]*dict_item[key][1])
    print("----------------------------------------------------------------------")

    #Showing the total purchase
    printYellow(f'Your total purchase is Rp {total}')

    #Using if to use the discount based on different conditions, and count the discounted price
    if total > 200000 and total <=300000:
        diskon = 5
        total = total*(100-diskon)/100
    elif total > 300000 and total <=500000:
        diskon = 8
        total = total*(100-diskon)/100
    elif total > 500000:
        diskon = 10
        total = total*(100-diskon)/100
    else: 
        diskon = 0
        total = total

    #Showing the discount the user get and the total discounted price
    printYellow(f'You get {diskon}% discount, you have to pay Rp {int(total)}')
    print("----------------------------------------------------------------------")

