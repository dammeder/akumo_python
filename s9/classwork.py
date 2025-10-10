
sentence = "Hey august batch, our sessions will be on saturday 10PM"

print(sentence[0:4])
print(sentence[-4:])
print(sentence[11:16])



num1 = int(input("first number = "))
div = int(input("divisible = "))

if num1 > 0 and num1 % div == 0: 
    print(f"{num1} is a positive number and is dvisible by {div}" )
elif num1 < 0 and  num1 % div == 0: 
    print(f"{num1} is a negative number and is dvisible by {div}" )
elif num1 > 0 and not num1 % div == 0: 
    print(f"{num1} is a positive number and is NOT dvisible by {div}" )
elif num1 < 0 and not num1 % div == 0: 
    print(f"{num1} is a negative number and is NOT dvisible by {div}" )


word = input("Enter your sentence: ")

if len(word) > 15: 
    print("The sentence is too big")
else:
    print(word)


