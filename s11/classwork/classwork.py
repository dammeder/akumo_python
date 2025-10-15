# >>>>>>>>>>>>>>>> SESSION 11 CLASSWORK <<<<<<<<<<<<<<<<<<

#    ⬇⬇⬇⬇⬇⬇  FOR ELSE, WHILE ELSE ⬇⬇⬇⬇⬇⬇

    # for i in range(1, 11):
    #     print(i)
    #     if i 
    # else:
    #     print("donneee")

    # counter = 10

    # while counter > 0:
    #     print(counter)
    #     counter -= 1
    # else: 
    #     print("done")

    # word = "this block gets exectied when the loop fulle finished"
    # character = input("Enter char: ")

    # for char in word:
    #     if character == word:
    #         break
    #     else:
    #         print(char)

    # for i in range(10):
    #     for j in range(1, 4):
    #         if j == 3:
    #             break
    #         else:
    #             print(j, end ='')

    #     break
    #     print()


    # for i in range(1, 11):
    #     if i % 2 == 0:
    #         print(i)
    #     else:
    #         pass
    #         print(i)

    # else:
    #     print("donneee")

# list1 = ["value1", "value2", "value3"]
# list1.append("value4")
# del list1[3]
# list1.insert(2, "value4")
# print(list1)
# list1.sort()
# print(list1)
# list1.sort(reverse = True)
# print(list1)


# num = int(input("enter a num - ")) 
# list_num = []

# for i in range(num + 1):
#     if i % 2 == 0:
#         list_num.append(i)
    
# print(list_num)   

# names = ["esen","meder","sunatullo","nurik","bob","esen", "meder"]
# print(names)
# inp = input("enter who you want to delete: ")

# for name in names:
#     if name == inp:
#         names.remove(name)    

# print(names)

# names = ["esen","meder","sunatullo","nurik","bob","esen","meder"]
# names.sort()
# print(names)
# ## names_new = names.copy()
# names_new = names[::]
# print(names_new)

# print(id(names))
# print(id(names_new))

#    ⬇⬇⬇⬇⬇⬇  LIST COMPREHENSION  ⬇⬇⬇⬇⬇⬇ 

list_comp = [i for i in range(1 , 11) if not i % 2 == 0]
print(list_comp)


inp = int(input("enter when to stop - "))

list_cubed = [i**3 for i in range(inp + 1)]
print(list_cubed)