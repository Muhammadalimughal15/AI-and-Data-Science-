def print_rangoli(size):
    width = 4 * size - 3
    for i in range(size):
        line = []
        for j in range(i):
            line.append(chr(96 + size - j))
        line.append(chr(96 + size - i))
        for j in range(i - 1, -1, -1):
            line.append(chr(96 + size - j))
        print("-".join(line).center(width, "-"))
    for i in range(size - 2, -1, -1):
        line = []
        for j in range(i):
            line.append(chr(96 + size - j))
        line.append(chr(96 + size - i))
        for j in range(i - 1, -1, -1):
            line.append(chr(96 + size - j))
        print("-".join(line).center(width, "-"))

n = int(input())
print_rangoli(n)