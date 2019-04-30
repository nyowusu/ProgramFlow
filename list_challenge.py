# alpha1 = ["A", "B", "C", "D"]
#
# alpha2 = ["A"]
# alpha2.append(["B"])
# alpha2.append(["C"])
# alpha2.append(["D"])
#
# print(alpha2)

my_list = list(range(1, 20, 2))
print(my_list)

for i in list(range(1, 20, 2)):
    my_list.append(i)

print(my_list)
print(my_list.index(1, 9, 13)) # what is the index of 1 between 9 and 13 or as described in the docs
                               # index of 1 after 9 before 13
# print(format(47, 'x'))
for i in range(257):
    print("{0:02} in binary is {0:08X}".format(i))
