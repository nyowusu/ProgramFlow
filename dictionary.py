fruit = {"orange": "a sweet, orange citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

veg = {"cabbage": "every child's favourite",
       "sprouts": "hmmmmm, lovely",
       "spinach": "may i have some fruit please"}


#
# print(fruit)
#
# fruit_itemview = fruit.items()
#
# fruit_2 = fruit.copy()
#
# # for r in range(10):
# #     for i in fruit_2:
# #         print((i, fruit_2[i]))
# #     print("="*50)
# print("="*40)
# print(fruit_itemview)
# print("="*40)
# # print(fruit_2)
# # popitem() - LIFO
# while len(fruit_2) > 0:
#     fruit_2.popitem()
#
# print(" The fruit_2 is: ", fruit_2)
# print("Loop finished")
#
# item = fruit.setdefault("pear", "a sweet, pear fruit")
# print(item)
# print("="*40)
# print(fruit_itemview)
# print("="*40)
# item = fruit.setdefault("orange")
# print(item)
# print("="*40)
# for i in fruit:
#     item = fruit.setdefault(i)
#     print(item)
# print("="*40)

# print(fruit)
# f_tuple = tuple(fruit.items())
# print(f_tuple)
# print("="*50)
# for item, desc in f_tuple:
#     print(item + " is " + desc)
#
# #print(dict(f_tuple)) # converts the tuple into a dictionary
#
# newString = ", "
# print("="*50)
# newString = ", ".join(fruit.keys())
#
# print(newString)
#
# print(veg)
#
# veggie = veg.copy()
#
# print(veggie)
#
# veggie.update(fruit)
#
# print(veggie)
print(veg)
print("="*100)
print(fruit)
print("="*100)

# copying fruits
nice_and_nasty = fruit.copy()
nice_and_nasty.update(veg)
print(nice_and_nasty)

