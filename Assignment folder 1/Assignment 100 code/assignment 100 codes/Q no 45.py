class American:
    def __init__(self, name):
        self.name = name

    def printNationality(self):
        print("American")

class NewYorker(American):
    def __init__(self, name, city):
        super().__init__(name)
        self.city = city

    def printCity(self):
        print(self.city)

# Testing the classes
new_yorker = NewYorker("John Doe", "New York")
new_yorker.printNationality()
new_yorker.printCity()