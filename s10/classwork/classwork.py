## #task 1 

# num = int(input("Enter your number - "))

# if num % 2 == 0: 
#     print("thats an even number you get there bucko")
# else:
#     print("clearly odd")

# ## task 2
# num1 = int(input("enter your number = "))

# if num1 > 0:
#     print("POSITIVE")
# elif num1 < 0:
#     print("NEGATIVE")
# else:
#     print("thats 0")

# ## task 3

# age = int(input("Enter your age - "))

# if age >= 18:
#     print("You are eligible to vote")
# else:
#     print("Youre not eligible to vote ")

# ## task 4

# word = input("Enter your word : ")
# char = input("Enter your character: ")

# if char in word:
#     print(f"The '{char}' character is inside your word")
# else:
#     print(f"The '{char}' character is not inside your word")

## task 5 

# int1 = int(input("first int = "))
# int2 = int(input("seconf int = "))

# if int1 > int2:
#     print(f"{int1} is larger than {int2}")
# elif int1 < int2:
#     print(f"{int2} is larger than {int1}")
# else:
#     print("theyre equal")

## task 6

# username = input("Username: ")
# passwd = input("Password: ")

# if username == "Admin" and passwd == "admin123":
#     print("Welcome Admin")
# else: 
#     print("Eroor: Unkown User or Incorrect Password")

# # FOR LOOPS

# for letter in "hello":
#     print(letter)

# for i in range(-10, 10, 2):
#     print(i)

## task 7

# num = int(input("Your interger: "))
# full_num = num + 1

# if num > 0:
#     if num % 2 == 0:
#         for i in range(0, full_num, 2):
#             print(i)
#     else:
#         for i in range(0, num, 2):
#             print(i)
# else:
#     print("Error")

## task 8

sentence = "The weather is great today"
char = input("Character = ")

counter = 0
if char in sentence:
    while sentence[counter] != char:
        print(sentence[counter])
        counter += 1


#     for i in sentence:
#         print(i)
#         if i == char:
#             break
else:
    print("No existing character inside of the string ")

