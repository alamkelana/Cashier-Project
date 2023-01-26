global dict_item 
dict_item = {}

def input_item():
    while True:
        nama_item = input("Input item name: ").strip().title()
        jumlah_item = int(input("Input total item: ").strip())
        harga_item = int(input("Input item price: ").strip())
        if nama_item in dict_item:
            print("\nError! Item already in your order")
        else:
            dict_item[nama_item] = [jumlah_item, harga_item]
        print("----------------------------------------------------------------------")
        while True:
            yn = input("Input another?? (Y/N): ").strip().lower()
            if yn == "y":
                break
            elif yn == "n":
                return
            else:
                print("\nPlease input Y/N only")
    print("----------------------------------------------------------------------")
    print("The item(s) was added successfully")
    print("----------------------------------------------------------------------")

input_item()