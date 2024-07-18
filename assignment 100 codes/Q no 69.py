import random
divisible_numbers = [i for i in range(10, 151) if i % 5 == 0 and i % 7 == 0]
print(random.choice(divisible_numbers))