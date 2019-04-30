import random

# string = "768273648564837"
#
# my_iter = iter(string)
#
# for n in range(0, len(string)):
#     char = next(my_iter)
#     if char in ["3","8"]:
#         print(char)

# my_list = list(range(10))
# print(my_list)
# random.shuffle(my_list)  #use of the shuffle function in random
# print(my_list)

# even = list(range(0, 10, 2))
# odd = list(range(1, 10, 2))
# print(even, odd)
#
# my_string="abcdefghijklmnopqrstuvwxyz123i9723986987309458"
# print(my_string.index('f'))
# print(my_string[4])
#
# small_decimals = range(1, 10)
# print(small_decimals)
# print(small_decimals.index(3))
#
# odd = range(1, 10000, 2)
# print(odd[985])

decimals = range(0, 100)
print(decimals)

my_range = decimals[3:40:3]
print(my_range)

for i in my_range:
    print(i)

print("=" * 40)

for i in range(3,40,3):
    print(i)
