"""
Create a simple calculator. The calculator should be able to perform 
basic math operations, add, subtract, divide and multiply. The calculator
should take input from users. The calculator should be able to handle
ZeroDivisionError, NameError, and ValueError.
"""

signs = ["+", "-", "/", "*"]


def calculator() -> int:
    try:
        num1 = int(input("(1) Enter a number: "))
        operator = input("Enter a sign (+, -, *, /): ")
        if operator not in signs:
            raise ValueError()
        num2 = int(input("(2) Enter a number: "))

        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "/":
            return num1 / num2
        elif operator == "*":
            return num1 * num2

    except ValueError:
        print("Enter a valid number or sign!")
        calculator()

    except ZeroDivisionError:
        print("Can't divide by 0")
        calculator()


print(calculator())
