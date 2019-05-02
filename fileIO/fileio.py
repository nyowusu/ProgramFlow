# jabber = open("sample.txt", 'r')
# my_jabber_list = list()
# for line in jabber:
#     my_jabber_list.append(line)
#
# jabber.close()
#
# for line in my_jabber_list:
#     print(line)

# the pythonic way
jabber = list()
with open("sample.txt", 'r') as f:
    for line in f:
        jabber.append(line)

print(jabber)
for line in jabber:
    print(line)
