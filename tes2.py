dict_item = {"Nasi":[5,5000], "Ayam":[3,30000]}

def delete_item():
    global dict_item
    print("1. Delete item \n2. Reset all transaction")
    delete = int(input("Choose delete type: ").strip())
    if delete == 1:
        item_delete = input("Input item name: ").strip().title()
        if item_delete in dict_item.keys():
            del dict_item[item_delete]
            print(dict_item)
        else: print(f"No present item with name {item_delete}")
    elif delete == 2:
        dict_item = {}
    else: print("Wrong input!")
    return dict_item

dict_item = delete_item()
print(dict_item)