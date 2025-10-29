# # def minus_one(num):
# #     if num == 0:
# #         print(num)
# #     else:
# #         print(num)
# #         minus_one(num - 1)

# # minus_one(10)


# # def factorial(num):
# #     if num == 1:
# #         return num
# #     else:
# #         return num * factorial(num - 1)

# # print(factorial(3))




# def plus_one(num):
#     if num == 0:
#         print(0)
#     else:
#         plus_one(num - 1)
#         print(num)

# plus_one(5)
# def plus_one(num)
#     if num > 0:
#         plus_one(num -1)

#     print(num)




students = {
    "Meder": {"batch":"aug25"},
    "Sunatullo": {"batch":"aug25"},
    "Nurik": {"batch":"aug25"}
}


try:
    inp = input("enter name: ").title()
    print(students[inp])


except KeyError:
    print("Student diesnt exist")
