# Task 3: Print a Word in a Pyramid Shape
# Input:
# Enter a word: CODE

# Output:
# C
# CO
# COD
# CODE

word = input("Enter word = ")

for i in range(1, len(word) + 1):
    print(word[:i])