def find_even_digit_numbers():
    even_digit_numbers = [str(i) for i in range(1000, 3001) if all(int(digit) % 2 == 0 for digit in str(i))]
    print(','.join(even_digit_numbers))

find_even_digit_numbers()