def f(n):
    if n == 0:
        return 0
    else:
        return f(n - 1) + 100

n = int(input("Enter a positive integer: "))
print(f(n))