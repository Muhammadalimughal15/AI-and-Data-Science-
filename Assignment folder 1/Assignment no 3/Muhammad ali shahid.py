# The amount of money initially was fifty dollars.

Money = 50

# The price of an item

Item_Price = 15

# Tax rate (3% is equal to 0.03)
Tax_Rate = 0.03

# Count the total cost of the item (price + tax)

Total_Cost = Item_Price + (Item_Price * Tax_Rate)

#Count how much money was left after buying the item

Money_Left = Money - Total_Cost

# Display the (result.)
print("You have $ ", round(Money_Left,2), " remainder after purchasing an item.")
