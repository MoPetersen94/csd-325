#Monika Petersen
#CSD205-300H
# 5/24/2026
#Module 11.2


# For the recursion method it calls itself until its at zero, then it starts printing all the way back up
def recursion(n):
    if n == 1:
        print(n)
        return
    recursion(n - 1)
    print(n)

# For non-recursion its just a for loop
def nonRecursion(n):
    for i in range(1, n + 1):
        print(i)

#Get a number from the user, go through recursion then non-recursion
number = input("Enter a whole, positive number: ")
# Checks if the input is a digit and greater than 0, if not it prints an error message and exits the program
if number.isdigit() and int(number) > 0:
    number = int(number)
else: 
    print("Invalid input. Please enter a whole, positive number.")
    exit()
print("Recursion:")
recursion(number)
print ("End of Recursion:")
print()
print()
print("Non-Recursion:")
nonRecursion(number)
print ("End of Non-Recursion:")
