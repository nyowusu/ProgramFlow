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
# jabber = list()
# with open("sample.txt", 'r') as f:
#     for line in f:
#         jabber.append(line)
#
# print(jabber)
# for line in jabber:
#     if 'JAB' in line.upper():
#         print(line, end='')

# with open("sample.txt", "r") as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end='')
#         line = jabber.readline()

with open("sample.txt", "r") as jabber:
    lines = jabber.readlines()
    # print(lines, end="")

set_unique_words = set()
for line in lines:
    print(line, end='')
    words = line.split(' ')
    # print(words)
    for word in words:
        if word.strip('\n') != '':
            set_unique_words.add(word.strip('\n')) #  only the unique words in the list
        # try:
        #     set_unique_words.add(word.strip())
        # except Exception:
        #     print("Error adding words to set")
print(set(sorted(set_unique_words)))


# writing to a new file called sample_copy
# with open("sample_copy.txt", "w") as jabberw:
#     jabberw.writelines(lines) #  this is one way to write to files
#     print("file written")

## the print function can be used to write to a file
with open("sample_copy.txt", "w") as jabberw:
    for line in lines:
        print(line, file=jabberw, end='')
