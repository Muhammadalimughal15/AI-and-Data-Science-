def print_square_dict():
    """
    Create a dictionary where the keys are numbers between 1 and 20 (both included)
    and the values are the squares of the keys.
    """
    square_dict = {}  # Initialize an empty dictionary

    for i in range(1, 21):  # Loop through numbers 1 to 20
        square_dict[i] = i ** 2  # Calculate the square of the number and add to the dictionary

    print("The dictionary with squares is:")
    for key, value in square_dict.items():  # Print the dictionary
        print(f"{key}: {value}")

# Call the function
print_square_dict()