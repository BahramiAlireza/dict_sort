dict_sorted=[]
def dict_sort(dict,key):
    key_collection=["{}-{}".format(dict[i][key],i) for i in range(len(dict))   ]
    key_sorted=sorted(key_collection)
    for i in range(len(key_sorted)):
        key,index=key_sorted[i].split("-")
        print(key,index)
        dict_sorted.append(dict[int(index)])
    print(dict_sorted)
