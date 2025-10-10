# Task 5: Triangle Type Checker
# Description:
#  Ask the user for 3 side lengths and determine what type of triangle they form:
# Equilateral: all sides equal
# Isosceles: two sides equal
# Scalene: all sides different
# Not a triangle: if the sum of any two sides is not greater than the third
# Example:
# Input: 5, 5, 5  
# Output: Equilateral triangle

get_sides = input("Enter the length of each side of your triagnle - ").split()
get_sides_int = list(map(int, get_sides))

a = get_sides_int[0]
b = get_sides_int[1]
c = get_sides_int[2]

if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("This is a equilateral triangle")
    elif (a == b ) or (a == c) or (b == c): 
        print("This is a Isosceles triangle")
    else: 
        print("This is a Scalene triangle")
    
else:
    print("not a valid triangle")    

