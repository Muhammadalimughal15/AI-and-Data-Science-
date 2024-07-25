def compute_series(n):
    result = 0.0
    for i in range(1, n + 1):
        result += i / (i + 1)
    return result

n = int(input("Enter a positive integer: "))
print(compute_series(n))