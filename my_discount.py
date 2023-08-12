"""
Create a function called my_discount. The function takes no 
arguments but asks the user to input the price and the 
discount (percentage) of the product. Once the user inputs the 
price and discount, it calculates the price after the discount. 
The function should return the price after the discount. 
"""


def my_discount():
    while True:
        try:
            price = int(input("Enter price: "))
            discount = int(input("Enter discount (%): "))
        except ValueError:
            print("Enter Valid Number")
        else:
            return price - (discount / 100 * price)


print(my_discount())
