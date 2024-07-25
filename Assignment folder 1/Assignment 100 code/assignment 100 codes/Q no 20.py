class DivisibleBySeven:
    def __init__(self, n):
        self.n = n

    def divisible_by_seven(self):
        for i in range(0, self.n + 1, 7):
            yield i

n = int(input("Enter a number: "))
divisible_by_seven = DivisibleBySeven(n)
for num in divisible_by_seven.divisible_by_seven():
    print(num)