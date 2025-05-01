#Title: Lab 11:
#Author: Jose Ocano
#Description: This lab will be about creating and reading grades in plain text files

#9.1 Assignment
print('Enter any number of grades: (-1 to stop)')
#open the txt file in write mode
file = open("grades.txt",'w')
#input the grades till user wishes to exit
while True:
    grade = int(input())
    if grade==-1:
        break
    else:
        file.writelines(f'{grade}\n')
    
#close the text file
file.close()

print("***************************************************************")

#9.2 Assignment

grades = None
#open the file and read the grades
with open('grades.txt', 'r') as file:
    grades = file.readlines()
    
#To store the sum of grades
total = 0

#Iterate over the grades and print it
for grade in grades:
    grade = int(grade.strip())
    print(grade)
    total += int(grade)

#Display the info as mentioned
print(f"Total: {total}")
print(f"Count: {len(grades)}")
print(f"Average: {total/len(grades) : .2f}")

print("***************************************************************")

#9.3 Assignment

import csv
#This will write student records to a CSV file
with open('grades.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)

#Create a header row
    csvwriter.writerow(["firstname", "lastname", "exam1grade", "exam2grade", "exam3grade"])
    
#This will collect student data
    while True:
        first_name = input("Enter first name (or 's' to stop): ")
        if first_name == 's':
            break
        last_name = input("Enter last name: ")
        exam1 = int(input("Enter exam 1 grade: "))
        exam2 = int(input("Enter exam 2 grade: "))
        exam3 = int(input("Enter exam 3 grade: "))

        #Assures that the student's record displays in the format right
        csvwriter.writerow([first_name, last_name, exam1, exam2, exam3])
        
print("Student records are saved to 'grades.csv'.")
        
