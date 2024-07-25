X, Y = map(int, input("Enter two comma-separated values for X and Y: ").split(','))

array_2d = [[i*j for j in range(Y)] for i in range(X)]

for row in array_2d:
    print(row)