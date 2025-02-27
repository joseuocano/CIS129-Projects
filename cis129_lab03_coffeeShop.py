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

#Make lines for the top border of receipt
print("***************************************************")

#Give a title for the coffee shop
print("Jose's Coffee Shop")


#Input: Number of coffees, muffins, teas, and sandwiches, the user is purchasing
num_coffees = int(input("Number of coffees bought? "))
num_muffins = int(input("Number of muffins bought? "))
num_teas = int(input("Number of teas bought? "))
num_sandwiches = int(input("Number of sandwiches bought? "))



#Calculate subtotals
subtotal_coffee = num_coffees * PRICEOF_COFFEE
subtotal_muffin = num_muffins * PRICEOF_MUFFIN
subtotal_tea = num_teas * PRICEOF_TEA
subtotal_sandwich = num_sandwiches * PRICEOF_SANDWICH
subtotal = subtotal_coffee + subtotal_muffin + subtotal_tea + subtotal_sandwich


#Calculate tax
tax = subtotal * TAX_RATE

#Calculate total
total = subtotal + tax




# Output: Display the receipt
print("****************************************************")
print()
print("Jose's Coffee Shop Receipt")
print(f"{num_coffees} Coffee(s) at ${PRICEOF_COFFEE:.2f} each: ${subtotal_coffee:.2f} ")
print(f"{num_muffins} Muffin(s) at ${PRICEOF_MUFFIN:.2f} each: ${subtotal_muffin:.2f} ")
print(f"{num_teas} Tea(s) at ${PRICEOF_TEA:.2f} each: ${subtotal_tea:.2f} ")
print(f"{num_sandwiches} Sandwich(es) at {PRICEOF_SANDWICH:.2f} each: {subtotal_tea:.2f} ")
print(f"6% tax: ${tax:.2f}")
print("------------------------------")
print(f"Total: ${total:.2f}") 
print(f"***************************************************")
print("\nThank you for visiting Jose's Coffee Shop! We hope that you visit us the next time!") 

