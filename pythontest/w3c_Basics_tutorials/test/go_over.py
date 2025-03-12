# import random
# x = random.randrange(0, 100, 5)
# print(x)

# y = range(0, 10, 2)
# print(list(y))

# for n in range(0, 10):
#     print(n)

# print(random.choice(list(y)))

# x = "艹 尼玛"
# y = reversed(x)
# z = x[::-1]
# print(y)
# print(z)
# print(list(y))

# list1 = [1, 2, 3, 4, 5, 1]
# set1 = set(list1)
# list2 = list(set1)
# print(set1, list2)
# list3 = dict.fromkeys(list1)
# print(list3)

# list4 = list(list3)
# print(list4)

# x = "xxx, wo ni ma"
# y = x.strip('x, ')
# print(y)
# # wo ni ma

list1 = [1, 2, 3, 4, 5, 1]
match list1:
    case _ if len(list1) > 6:
        print("list1 has more than 6 elements")
    case _ if len(list1) > 6:
        print("list1 has more than 6 elements")
    case _:
        print("list1 has 6 or fewer elements")

x = 69
match x:
    case 0:
        print("x value is 0")
    case x if x > 0:
        print("x value is greater than 0")
    case _ :
        print("x value is less than 0")