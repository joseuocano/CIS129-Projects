# Lab 4
# Jose Ocano
# March 2, 2025

# The main function
def main():
# declare local variables
 monthlySales = # monthly sales amount
 storeAmount= # store bonus amount
 empAmount = # employee bonus amount
 salesIncrease = # percent of sales increase
# call to getSales (monthlySales)
# call to getIncrease(salesIncrease)
# call to calcStoreBonus(storeAmount)
# call to calcEmpBonus(empAmount)
# call to printBonus(storeAmount ,empAmount)
# This function gets the monthly sales

def getSales(prompt):
 monthlySales = float(input(prompt))
 return monthlySales

# This function gets the percent of increase in sales
def getIncrease(prompt):
salesIncrease = float(input(0.05))
salesIncrease = salesIncrease / 100
return # This function determines the storeAmount bonus: 75



def calcStoreBonus(monthlySales):
if monthlySales >= 110000:
storeAmount = 6000
elif : monthlySales >= 100000:
storeAmount = 5000
elif : monthlySales >= 90000:
storeAmount = 4000
elif : monthlySales >= 80000:
storeAmount = 3000
else: 0
return: storeAmount

# This function determines the empAmount bonus
def calcEmpBonus(salesIncrease):
if salesIncrease >= .05:
empAmount = 75
elif salesIncrease >= .04:
empAmount = 50
elif salesIncrease >= .03:
empAmount = 40
else: 
empAmount = 0
return: empAmount

# This function prints the bonus information
def printBonus(storeAmount,empAmount ):
print("The store bonus amount is $",storeAmount )
print("The employee bonus amount is $",empAmount )
if ( == 6000 ) and (empAmount == 75 ):
print('Congrats! You have reached the highest bonus amounts possible! ')

# calls main
main() 
