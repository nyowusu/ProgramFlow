# decimals = range(0, 100)
# my_range = decimals[3:40:3]
# print(my_range == range(3, 40, 3))
# print(range(0,5,2) == range(0,6,2))
#
# r = range(0, 100)
# print(r)
#
# for i in r[::-3]:
#     print(i)
# print(r[::-2] == range(99,0,-2))
# for i in range(99, 0, -2):
#     print(i)
# print("="*50)
# print(range(0, 100)[::-2] == range(99, 0, -2))
#
# for i in range(1000, 100, -2):
#     print(i)

# USES OF A NEGATIVE SLICE reverses the string
# backString = "egauganl lufrewop yerv a si nohtyp"
# print(backString[::-1])

backString = ""
forwardString = "Python is a very powerful language"
for i in forwardString[::-1]:
    backString += i
print(backString)
print(backString[::-1])

print("="*40)

r = range(0, 10)
for i in r[::-1]:
    print(i)