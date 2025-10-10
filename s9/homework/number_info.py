# Task 1: Number info
# Description:
#  Ask the user to enter a number. Your program should:
# Check if the number is positive, negative, or zero
# Check if the number is even or odd
# Print both results
# Example:
# Input: -11  
# Output:
# The number is negative  
# The number is odd

num = int(input("Enter number - "))

if num > 0:
    print("Number is postive")
elif num < 0:
    print("Number is negative")
else: 
    print("Number is 0")

if num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")