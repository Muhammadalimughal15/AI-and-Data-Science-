my_list = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
unique_list = list(set(my_list))
unique_list.sort(key=my_list.index)
print(unique_list)