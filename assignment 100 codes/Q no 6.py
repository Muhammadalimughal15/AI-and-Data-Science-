import math

C = 50
H = 30

D_values = input("Enter a sequence of comma-separated values for D: ")
D_values = list(map(int, D_values.split(',')))

Q_values = []
for D in D_values:
    Q = round(math.sqrt((2 * C * D) / H))
    Q_values.append(str(Q))

print(','.join(Q_values))