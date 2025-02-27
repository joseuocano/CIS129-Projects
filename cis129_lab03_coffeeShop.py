# Program: Jose's Coffee Shop Simulator
# Description: A basic interactive text-based coffee shop simulator that calculates the receipt of the customer
# Author: Jose Ocano
# Date: February 23, 2025

# Constants
PRICEOF_COFFEE = 5.00
PRICEOF_MUFFIN = 4.00
PRICEOF_TEA = 3.00
PRICEOF_SANDWICH = 7.00
TAX_RATE = 0.06

# Integers
a = "2"
b = "3"
c = "1"
d = "4"

#Make lines for the top border of receipt
print("***************************************************")

#Give a title for the coffee shop
print("Jose's Coffee Shop")


#Input: Number of coffees, muffins, teas, and sandwiches, the user is purchasing
num_coffees = "Number of coffees bought?"
print(num_coffees)
print(a)
num_muffins = "Number of muffins bought?"
print(num_muffins)
print(b)
num_teas = "Number of teas bought?"
print(num_teas)
print(c)
num_sandwiches = "Number of sandwiches bought?"
print(num_sandwiches)
print(d)

#Calculate subtotals
subtotal_coffee = int(a) * PRICEOF_COFFEE
subtotal_muffin = int(b) * PRICEOF_MUFFIN
subtotal_tea = int(c) * PRICEOF_TEA
subtotal_sandwich = int(d) * PRICEOF_SANDWICH
subtotal = subtotal_coffee + subtotal_muffin + subtotal_tea + subtotal_sandwich


#Calculate tax
tax = subtotal * TAX_RATE

#Calculate total
total = subtotal + tax




# Output: Display the receipt
print("****************************************************")
print()
print("Jose's Coffee Shop Receipt")
print(f"{int(a)} Coffee(s) at ${PRICEOF_COFFEE:.2f} each: ${subtotal_coffee:.2f} ")
print(f"{int(b)} Muffin(s) at ${PRICEOF_MUFFIN:.2f} each: ${subtotal_muffin:.2f} ")
print(f"{int(c)} Tea(s) at ${PRICEOF_TEA:.2f} each: ${subtotal_tea:.2f} ")
print(f"{int(d)} Sandwich(es) at ${PRICEOF_SANDWICH:.2f} each: ${subtotal_sandwich:.2f} ")
print(f"6% tax: ${tax:.2f}")
print("------------------------------")
print(f"Total: ${total:.2f}") 
print(f"***************************************************")
print("\nThank you for visiting Jose's Coffee Shop! We hope that you visit us the next time!") 
