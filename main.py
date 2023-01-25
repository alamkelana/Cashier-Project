import project

dict_item = {}
print("Welcome!")

while True:
    print("\nMAIN MENU")
    print("1. Input item \n2. Update item \n3. Delete item \n4. Check order \n5. Checkout your order\n")
    menu = int(input("What would you like to do? (input a number based on the menu above): ").strip())
    print("")
    if menu == 1:
        dict_item = project.input_item()
    elif menu == 2:
        dict_item = project.update_item()
    elif menu == 3:
        dict_item = project.delete_item()
    elif menu == 4:
        project.check_order()
    elif menu == 5: 
        project.total_price()