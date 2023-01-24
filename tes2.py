dict_item = {"Nasi Goreng": [24, 20000], "Ayam Goreng" : [1,30000]}

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
