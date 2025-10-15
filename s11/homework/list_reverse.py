# Task 1: Reverse a List
# Write a program that reverses a list using a for loop.
# Example:

# Input:
# Enter numbers separated by space: 1 2 3 4 5
# Output:
# Reversed List: [5, 4, 3, 2, 1]

inp = (input("Enter numbers seperated by spaces: "))
int_list = [int(num) for num in inp.split()]
int_list.reverse()

print(int_list)

