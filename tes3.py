dict_item = {"nasi goreng": [2,20000], "ayam goreng": [3,30000]}

list = [i[0]*i[1] for i in dict_item.values()] 
print(list)