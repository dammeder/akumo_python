# Task 2: Reverse a Word using for loop (please don’t reverse a string using word[::-1])
# Input:
# Enter a word: Python
# Output:
# Reversed Word: nohtyP


word = input("enter a word: ")
reversed_word = ""

for char in word:
    reversed_word = char + reversed_word

print(reversed_word)