# fungsi buat ID transaksi


# fungsi masukkin item, pake dict nama item: [jumlah, harga]
dict_item = {}
def input_item():
    while True:
        nama_item = input("Masukkan nama item: ").strip().title()
        jumlah_item = int(input("Masukkan jumlah item: ").strip())
        harga_item = int(input("Masukkan harga item: ").strip())
        dict_item[nama_item] = [jumlah_item, harga_item]
        yn = input("input item lain? (y/n): ").strip().lower()
        if yn == "y":
            pass
        elif yn == "n":
            break
        else:
            print("Wrong Input!!!")
            break
    print(dict_item)

# fungsi update item, ada 3 opsi: update item, update jumlah, update harga
def update_item():
    print("1. Update item \n2. Update jumlah \n3. Update harga ")
    update = int(input("pilih jenis update: ").strip())
    if update == 1:
        update_item = input("masukkan nama item yang ingin diupdate: ").strip().title()
        if update_item in dict_item.keys():
            updated_item = input("masukkan update item: ").strip().title()
            dict_item[updated_item] = dict_item[update_item]
            del dict_item[update_item]
            print(dict_item)
        else: 
            print(f"tidak ada item dengan nama {update_item}")
    elif update == 2:
        update_jumlah = input("masukkan nama item yang ingin diupdate jumlahnya: ").strip().title()
        if update_jumlah in dict_item.keys():
            updated_jumlah = int(input("masukkan jumlah item baru: ").strip())
            dict_item[update_jumlah][0] = updated_jumlah
            print(dict_item)
        else: print(f"tidak ada item dengan nama {update_jumlah}")
    elif update == 3:
        update_harga = input("masukkan nama item yang ingin diupdate harganya: ").strip().title()
        if update_harga in dict_item.keys():
            updated_harga = int(input("masukkan harga item baru: ").strip())
            dict_item[update_harga][1] = updated_harga
            print(dict_item)
        else: print(f"tidak ada item dengan nama {update_harga}")
    else: print("Wrong Input!")

# fungsi delete item, ada 2 opsi: delete item pake nama, reset transaction apus semua
def delete_item():
    print("1. delete item \n2. reset all transaction")
    delete = int(input("pilih jenis delete: ").strip())
    if delete == 1:
        item_delete = input("masukkan nama item yang mau di-delete: ").strip().title()
        if item_delete in dict_item.keys():
            del dict_item[item_delete]
            print(dict_item)
        else: print(f"tidak ada item dengan nama {item_delete}")
    elif delete == 2:
        dict_item = dict()
    else: print("Wrong input!")


# fungsi check order, pemesanan benar kalo order sudah lengkap, pemesanan
# belum benar kalau order ada yg kosong, keluarin output hasil transaksi dlm bentuk tabel
def check_order():
    print("{:<15} {:<15} {:<15} {:<15}".format("Nama Item", "Jumlah Item", "Harga Item", "Total"))
    for key in dict_item.keys():
        print("{:<15} {:<15} {:<15} {:<15}".format(key, dict_item[key][0], dict_item[key][1],dict_item[key][0]*dict_item[key][1]))

# fungsi total price, tambahin branching ketentuan diskon
def total_price():
    total = 0
    for key in dict_item.keys():
        total = total+(dict_item[key][0]*dict_item[key][1])
    print(f'Total belanja anda adalah {total}')
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
    print(f'Anda mendapatkan diskon sebesar {diskon}%, total yang harus dibayarkan adalah {total}')
