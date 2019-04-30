a = b = c = d = 12 # assignment is evaluated from right to left
print(c)

a, b = 12, 13
print("a is {}".format(a))
print("b is {}".format(b))

a, b = b, a
print("a is {}".format(a))
print("b is {}".format(b))
