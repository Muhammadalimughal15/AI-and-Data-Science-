# Print documentation for built-in functions
print("abs() function documentation:")
print(abs.__doc__)
print()

print("int() function documentation:")
print(int.__doc__)
print()

print("input() function documentation:")
print(input.__doc__)
print()

# Define a class with a class parameter and an instance parameter
class MyClass:
    class_parameter = "This is a class parameter"

    def __init__(self, instance_parameter):
        self.instance_parameter = instance_parameter

    def my_method(self):
        """This is a custom method that prints the instance parameter"""
        print("Instance parameter:", self.instance_parameter)

    def __str__(self):
        return f"MyClass instance with instance parameter {self.instance_parameter}"

# Create an instance of the class
my_object = MyClass("This is an instance parameter")

# Print the documentation for the custom method
print("my_method() function documentation:")
print(my_object.my_method.__doc__)
print()

# Print the class parameter and instance parameter
print("Class parameter:", MyClass.class_parameter)
print("Instance parameter:", my_object.instance_parameter)
print()

# Print the object's string representation
print("Object representation:", my_object)