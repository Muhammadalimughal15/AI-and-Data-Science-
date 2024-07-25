def square_odd_numbers():
    numbers = input("Enter a sequence of comma-separated numbers: ")
    numbers = [int(x) for x in numbers.split(',')]
    squared_odd_numbers = [str(x ** 2) for x in numbers if x % 2 != 0]
    print(','.join(squared_odd_numbers))

square_odd_numbers()