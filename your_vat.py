"""
Write a function called your_vat. The function takes no 
parameter. The function asks the user to input the price of an 
item and VAT (vat should be a percentage). The function should 
return the price of the item plus VAT.
Make sure that your code can handle ValueError. Ensure the 
code runs until valid numbers are entered. (hint: Your code 
should include a while loop).
"""


def your_vat() -> float:
    while True:
        try:
            price = int(input("Price of Item: "))
            vat = int(input("VAT(%): "))
        except ValueError:
            print("Enter a valid number")
        else:
            return (vat / 100 * price) + price


print(your_vat())
