from tabulate import tabulate
dict_item = {"nasi goreng": [2,20000], "ayam goreng": [3,30000]}
print_dict = {"Item Name" : [i for i in dict_item.keys()],
            "Total Item": [i[0] for i in dict_item.values()],
            "Price": [i[1] for i in dict_item.values()],
            "Total": [i[0]*i[1] for i in dict_item.values()]}

print(tabulate(print_dict, headers = "keys", tablefmt = "github"))