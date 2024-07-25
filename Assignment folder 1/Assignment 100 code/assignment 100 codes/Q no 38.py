# python
t = (1,2,3,4,5,6,7,8,9,10)
even_numbers = [i for i in t if i % 2 == 0]
even_tuple = tuple(even_numbers)
print("The tuple of even numbers is:", even_tuple)