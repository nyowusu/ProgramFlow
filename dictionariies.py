fruit = {"orange":"a sweet, orange citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

# print(fruit)
# print("="*50)
# print(fruit["orange"])
# print("="*50)
# fruit["orange"] = "red on the inside, a sweet, orange citrus fruit"
# print(fruit)
# print("="*50)
# print(fruit["lime"])
# print("="*50)
# print("key","\t\t","Value")
# print("===","\t\t","=====")
# for key in fruit.keys():
#     print(key,"\t\t",fruit[key])
# print("="*50)
# for value in fruit.values():
#     print(value)
# print("="*50)
# fruit["peer"] = "an odd shaped apple" # this adds a new key:value pair to a dictionary
#                                       # keys are immutable
# print("key","\t\t","Value")
# print("===","\t\t","=====")
# for key in fruit.keys():
#     print(key,"\t\t",fruit[key])
# print("="*50)
# # sorted(fruit, reverse=True)
# del fruit
# print("key","\t\t","Value")
# print("===","\t\t","=====")
# for key in fruit.keys():
#     print(key,"\t\t",fruit[key])
# print("="*50)

# using the get function on the dictionary does not give an error if the key does not exist.

while True:
    dic_key = input("Enter a fruit: ")
    if dic_key in ["quit", "Quit"]:
        break
    if dic_key in fruit:
        description = fruit.get(dic_key)
        print(description)
    else:
        print("We don't have {}".format(dic_key))
