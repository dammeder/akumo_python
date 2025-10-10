# Task 3: Password Validator
# Description:
#  Ask the user to input a password.
#  Check if it meets all of the following conditions:
# At least 8 characters long
# Contains the letter “@”
# Does not contain any spaces
# Print:
# "Strong password" if all conditions are met
# Otherwise, print "Weak password"
# Example:
# Input: hello@123  
# Output: Strong password

passwd = input("Enter your password: ")

if "@" in passwd and len(passwd) >= 8 and not " " in passwd:
    print("Strong passwrod")
else:
    print("Weak password")