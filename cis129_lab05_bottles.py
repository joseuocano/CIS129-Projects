
# Title: Lab 5
# Name: Jose Ocano
# Date: March 11, 2025
# Purpose: This program calculates the total number of bottles collected







# Declare variables
totalBottles = 0
totalPayout = 0
todayBottles = 0
counter = 1
keepGoing = "y"
NBR_OF_DAYS = 7


# function to read today bottles count the return total bottles
def getBottles():
    counter = 1    # set the counter to 1
    totalBottles = 0    # set totalBottles initially to 0
    
    
    # while counter is less than or equal to 7
    while counter<=7:
        # read today bottles count as int
        todayBottles = int(input("Enter number of bottles for day: "))
        # then sum it into the totalBottles count
        totalBottles = totalBottles + todayBottles
        # increment the counter
        counter = counter + 1

    # return totalBottles
    return totalBottles

# function to calculate the total payment
def calcPayment(totalBottles):
    # calculate the total payout by multiplying by 0.10
    totalPayout = totalBottles * .10
    # return the totalPayout
    return totalPayout

# function to print the info
def printInfo(totalBottles, totalPayout):
    # print all info
    print("The total number of bottles collected is:", totalBottles)
    # here %.1f is used to precise the totalPayout to 1 decimal place
    print("The total paid out is $%.1f" %totalPayout)

# main() function
def main():
    # initially set keepGoing to "y"
    keepGoing= "y"
    # loop control using keepGoing
    while keepGoing == "y":
        # call the getBottles() to get totalBottles
        totalBottles = getBottles()
        # call calcPayment to calculate the total payout
        totalPayout = calcPayment(totalBottles)
        # call the printInfo to print all details
        printInfo(totalBottles, totalPayout)
        # ask if the user  wants to enter another week's worth of data
        keepGoing = input("Do you want to enter another week's worth of data? (Enter y or n): ")
        print("")


# call main() function
main()

