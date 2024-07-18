def add_string_numbers(str_num1, str_num2):
    """
    Receive two integer numbers in string form, compute their sum, and print it to the console.

    Args:
        str_num1 (str): The first number as a string.
        str_num2 (str): The second number as a string.
    """
    num1 = int(str_num1)  # Convert string to integer
    num2 = int(str_num2)  # Convert string to integer
    sum = num1 + num2
    print("The sum of", str_num1, "and", str_num2, "is:", sum)

# Test the function
str_num1 = "5"
str_num2 = "3"
add_string_numbers(str_num1, str_num2)