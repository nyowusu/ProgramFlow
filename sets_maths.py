# # mathematical operations with sets
#
# evens = set(range(0, 40, 2))
# multiples_3 = set(range(0, 40, 3))
# print(evens)
# print(multiples_3)
#
# print(evens.isdisjoint(multiples_3))
# print(evens.intersection(multiples_3))
#
# # in evens but not in multiples_3
# print(evens.difference(multiples_3))
#
# # in multiples_3 but not in evens
# print(multiples_3.difference(evens))
#
# # in evens and multiples_3 but not both
# print(evens.symmetric_difference(multiples_3))
#
# print(set('abc').intersection('cbs'))
# print(set('abc').intersection('cbs'))
#
# # removes elements if not present raises KeyError error
# try:
#     evens.remove(5)
# except KeyError:
#     print("The element does not exist")
#
# # removes elements if not present does not raise error
# print("Length of evens {}".format(len(evens)))
# evens.discard(3)
# print("Length of evens {}".format(len(evens)))


my_dict = {1: "one", 2: "two", 3: "three"}
print(my_dict)

print("="*50)
temp = {4: "four", 5: "five", 6: "six"}
my_dict.update(temp)
print(my_dict)

print("="*50)
my_dict.update(y="seven", p="eight")
print(my_dict)

print("="*50)
my_list = list()

for key in my_dict:
    my_list.append((key,my_dict[key]))

print("="*50)
print(my_list)

print("="*50)
my_list.pop()
dict_2 = dict(my_list)
print(dict_2)
