# Ask the user how many days until their birthday
days_until_birthday = int(input("How many days until your birthday? "))

# Calculate the approximate number of weeks until their birthday
weeks_until_birthday = days_until_birthday // 7

# Print the result
print("There are approximately {} weeks until your birthday.".format(weeks_until_birthday))