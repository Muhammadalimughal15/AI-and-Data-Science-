def concatenate_strings(str1, str2):
    """
    Accept two strings as input, concatenate them, and print the result to the console.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.
    """
    concatenated_str = str1 + str2  # Concatenate the strings using the + operator
    print("The concatenated string is:", concatenated_str)

# Test the function
str1 = "Hello, "
str2 = "World!"
concatenate_strings(str1, str2)