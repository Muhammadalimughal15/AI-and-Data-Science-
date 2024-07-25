for rabbits in range(36):
    chickens = 35 - rabbits
    if 2 * rabbits + 4 * chickens == 94:
        print(f"Rabbits: {rabbits}, Chickens: {chickens}")
        break