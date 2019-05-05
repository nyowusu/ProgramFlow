# serialization is the saving of an object in the binary for
# and re-reading and re-creating the object in the.
# This is stored with some data to help in the recreation of the object.
# Serialization in python is pickling.

import pickle  #  the pickle module is imported to pickle objects

# creating a tuple
imelda = "More Mayhem", "Imelda May", "2011", (
    (1, "Pulling the Rug"), (2, "Pscyho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

# this tuple with be stored in a binary file using pickling

with open("imelda.pickle", "bw") as file:
    pickle.dump(imelda, file)

with open("imelda.pickle", "br") as file:
    imelda_2 = pickle.load(file)
    print(imelda_2)
