# Task 2: Final Decision
# Description:
#  Take two boolean inputs from the user (True or False) and show the result of and, or, and not operations.
# Example:
# Input:
# First Boolean: True  
# Second Boolean: False  
# Output:
# True and False = False  
# True or False = True  
# not True = False

bool1 = eval(input("Enter first boolean value ( True / False ): "))
bool2 = eval(input("Enter second boolean value ( True / False ): "))

result1 = bool1 and bool2

print(f"{bool1} and {bool2} = {bool1 and bool2} ")
print(f"{bool1} or {bool2} = {bool1 or bool2} ")
print(f"not {bool1} = {not bool1}")

