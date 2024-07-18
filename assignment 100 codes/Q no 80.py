my_list = [12, 24, 35, 70, 88, 120, 155]
my_list = [val for idx, val in enumerate(my_list) if idx not in [0, 2, 4, 6]]
print(my_list)