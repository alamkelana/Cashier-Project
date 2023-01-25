# fungsi buat ID transaksi


# fungsi masukkin item, pake dict nama item: [jumlah, harga]
dict_item = {}
def input_item():
    global dict_item
    try:
        while True:
            nama_item = input("Input item name: ").strip().title()
            jumlah_item = int(input("Input total item: ").strip())
            harga_item = int(input("Input item price: ").strip())
            dict_item[nama_item] = [jumlah_item, harga_item]
            yn = input("Input another?? (Y/N): ").strip().lower()
            if yn == "y":
                continue
            elif yn == "n":
                break
            else:
                print("\nWrong Input!!!")
                break
        return dict_item
    except:
        print("\nWrong input!!!")
    
# fungsi update item, ada 3 opsi: update item, update jumlah, update harga
def update_item():
    global dict_item
    print("1. Update item name \n2. Update total item \n3. Update item price ")
    update = int(input("Choose update type: ").strip())
    if update == 1:
        update_item = input("Input item name that you'd like to update: ").strip().title()
        if update_item in dict_item.keys():
            updated_item = input("Input new item name: ").strip().title()
            dict_item[updated_item] = dict_item[update_item]
            del dict_item[update_item]
        else: 
            print(f"No present item with name {update_item}")
    elif update == 2:
        update_jumlah = input("Input item name that you'd like to update: ").strip().title()
        if update_jumlah in dict_item.keys():
            updated_jumlah = int(input("Input new total item: ").strip())
            dict_item[update_jumlah][0] = updated_jumlah
        else: print(f"No present item with name {update_jumlah}")
    elif update == 3:
        update_harga = input("Input item name that you'd like to update: ").strip().title()
        if update_harga in dict_item.keys():
            updated_harga = int(input("Input new item price: ").strip())
            dict_item[update_harga][1] = updated_harga
        else: print(f"No present item with name {update_harga}")
    else: print("\nWrong Input!")
    return dict_item

# fungsi delete item, ada 2 opsi: delete item pake nama, reset transaction apus semua
def delete_item():
    global dict_item
    print("1. Delete item \n2. Reset all transaction")
    delete = int(input("Choose delete type: ").strip())
    if delete == 1:
        item_delete = input("Input item name: ").strip().title()
        if item_delete in dict_item.keys():
            del dict_item[item_delete]
        else: print(f"No present item with name {item_delete}")
    elif delete == 2:
        dict_item = {}
    else: print("\nWrong input!")
    return dict_item


# fungsi check order, pemesanan benar kalo order sudah lengkap, pemesanan
# belum benar kalau order ada yg kosong, keluarin output hasil transaksi dlm bentuk tabel
def check_order():
    print("{:<15} {:<15} {:<15} {:<15}".format("Item Name", "Total Item", "Item Price", "Total"))
    for key in dict_item.keys():
        print("{:<15} {:<15} {:<15} {:<15}".format(key, dict_item[key][0], dict_item[key][1],dict_item[key][0]*dict_item[key][1]))

# fungsi total price, tambahin branching ketentuan diskon
def total_price():
    total = 0
    for key in dict_item.keys():
        total = total+(dict_item[key][0]*dict_item[key][1])
    print(f'Your total is {total}')
    if total > 20000 and total <=300000:
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
    print(f'You get a {diskon}% discount, you have to pay Rp {total}')
