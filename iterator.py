string = ['123456', '23456', '72948', '76289', 'spam', 3456]

my_iterator = iter(string)
# print(my_iterator)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator)) #raises an error
#
# for char in string:
#     print(char)
#
# for char in iter(string):
#     print(char)

for n in range(0, len(string)):
    print(next(my_iterator))
