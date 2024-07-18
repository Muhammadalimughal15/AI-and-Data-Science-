# python
def generate_and_print_squares_tuple():
    square_list = []
    for i in range(1, 21):
        square_list.append(i ** 2)
    square_tuple = tuple(square_list)
    print("The tuple of squares is:", square_tuple)

generate_and_print_squares_tuple()