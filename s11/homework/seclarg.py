# Task 4: Find the Second Largest Number in a List (No max() or sort())
# Ask the user to enter a list of numbers. Find and print the second largest number without using max() or sort().

# Example:
# Enter numbers: 10 45 78 23 89 56  
# Second largest number: 78

list_inp = (input("Enter a list of numbers:"))
list_num = [int(num) for num in list_inp.split()]

print(list_num)
largest_num = max2 = float('-inf')

for num in list_num:
    if num > largest_num:
        max2 = largest_num
        largest_num = num

    elif num > max2 and num != largest_num:
        max2 = num
    
print(' ')
print(max2)