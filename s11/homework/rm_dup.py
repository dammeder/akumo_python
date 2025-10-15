# Task 2: Remove Duplicates from a List
# Ask the user to enter multiple words separated by spaces. Store them in a list and remove duplicate words while maintaining the original order.

# Example:
# Enter words: apple banana apple cherry banana apple  
# Filtered List: ['apple', 'banana', 'cherry']


inp = input("Enter words seperated by spaces: ")
inp_list = inp.split()
unique_list = []

for i in inp_list:
    if i not in unique_list:
        unique_list.append(i)

print(inp_list)
print(unique_list)
