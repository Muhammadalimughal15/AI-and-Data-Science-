def count_case_letters():
    sentence = input("Enter a sentence: ")
    upper_case = sum(1 for c in sentence if c.isupper())
    lower_case = sum(1 for c in sentence if c.islower())
    print(f"UPPER CASE {upper_case}")
    print(f"LOWER CASE {lower_case}")

count_case_letters()