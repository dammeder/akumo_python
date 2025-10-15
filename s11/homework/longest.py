# Task 3: Find the Longest Word in a List
# Ask the user to enter a list of words. Find and print the longest word from the list.

# Example:
# Enter words: Python Java JavaScript C  
# Longest word: JavaScript  

inp = (input("Enter words seperated by spaces: ")).split()
longest_word = ""

for i in inp:
    if len(i) > len(longest_word):
        longest_word = i

print(len(longest_word), longest_word)
