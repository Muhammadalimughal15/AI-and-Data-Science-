def check_divisible_by_five():
    binary_numbers = input("Enter comma separated 4 digit binary numbers: ").split(',')
    divisible_numbers = [num for num in binary_numbers if int(num, 2) % 5 == 0]
    print(','.join(divisible_numbers))

check_divisible_by_five()