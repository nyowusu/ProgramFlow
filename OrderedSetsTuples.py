# t = "a", "b", "c" #it doesn't really matter if the parenthesis are added or not.
# print(t)            # it is still a tuple
#
# print("a", "b", "c")
# print(("A", "B", "C")) # to print a tuple or spread it over a multiple lines use brackets
# t2 = ("a", 1, "c", "a")
#
# print(t2)

# tuples are immutable meaning the content cannot be changed after it has been created
# but the variable can to assigned a different tuple
# a list is a mutable object meaning the content can be changed.
# list are intended to hold monogenous data
# tuples are intended to hold heterogenous data
welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "NightFlight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the lightening", "Metallica", 1984

# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])
#
# print(imelda)
# imelda = imelda[0], "Imelda", imelda[2]
#
# print(imelda)

metallica2 = list(metallica)
print(metallica2)

title, artist, year = metallica2 # this is the principle of unpacking a list
                                # unpacking is mostly useful for immutable objects hence its not good to unpack lists
                                # list are subject to change
print(title)
print(artist)
print(year)

title, artist, year = welcome  # this is the principle of unpacking tuples

print(welcome)
print(title)
print(artist)
print(year)
print("=" *40)
# checking if a sequence of a string can also be unpacked
my_abc = "ABC"
a, b, c = my_abc
print(my_abc)
print(a)
print(b)
print(c)
# the above code shows that you can unpack any sequence of data given the right number of variables on the left.
print("x"*50)
# imelda has been modified to contain a tuple
imelda = "More Mayhem", "Emilda May", 2011, ((1, "track1"), (2, "track2"), (3, "track3"))
print(imelda)
print("Unpackting Imelda", "="*40)
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
print(tracks)
print("looping throught the tuple", "="*50)
for i in tracks:
    print(i)
    tnum, tname = i
    print(tnum, " ", tname)
print("="*60)
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
print("\tTracks:")
for tnum, tname in tracks:
    #print("\t", tnum, " ", tname)
    print("\tTrack number: {}, Title: {}".format(tnum, tname))
