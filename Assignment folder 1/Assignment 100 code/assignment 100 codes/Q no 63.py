def divisible_by_5_and_7(n):
    for i in range(n+1):
        if i % 5 == 0 and i % 7 == 0:
            yield i

n = int(input("Enter a number: "))
print(','.join(map(str, divisible_by_5_and_7(n))))