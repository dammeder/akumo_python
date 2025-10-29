
# def search(list_num, digit):
#     for index in range(len(list_num)):
#         if list_num[index] == digit:
#             return index
#             break
#     return 'Digit does not exist'

    


# lst = [1,2,3,1,3,4,5,23,423,24]
# print(search(lst, 100))



def pyramid(word):
    for i in range(1, len(word) + 1):
        print(word[:i])

pyramid("hello people")


print('hello world')