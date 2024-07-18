import addition
import subtraction
import multiplication
import division

def calculator():
    while True:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter the operator (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        if operator == "+":
         result = addition.add(num1, num2)
        elif operator == "-":
            result = subtraction.subtract(num1, num2)
        elif operator == "*":
            result = multiplication.multiply(num1, num2)
        elif operator == "/":
            result = division.divide(num1, num2)
        else:
            print("Invalid operator. Please try again.")
            continue

        print("Result: ", result)

        response = input("Do you want to quit the calculator? (Y/N): ")
        if response.upper() == "Y":
            break

if __name__ == "__main__":
    calculator()
