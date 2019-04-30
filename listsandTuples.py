# this is the try modify a list in a tuple

imelda = "More Mayhem", "Emilda May", 2011, [(1, "track1"), (2, "track2"), (3, "track3")]

print(imelda)

print(imelda[3])
imelda[3].append(("4", "track4"))
print(imelda[3])
imelda[3].append(("5", "track5"))
print(imelda)
print("="*60)
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
print("\tTracks:")
for tnum, tname in tracks:
    #print("\t", tnum, " ", tname)
    print("\tTrack number: {}, Title: {}".format(tnum, tname))


