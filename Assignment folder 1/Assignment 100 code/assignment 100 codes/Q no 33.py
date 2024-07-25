# python
def generate_and_print_squares():
    square_list = []
    for i in range(1, 21):
        square_list.append(i ** 2)
    print("The first 5 elements in the list are:", square_list[:5])

generate_and_print_squares()