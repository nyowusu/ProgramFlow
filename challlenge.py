# take input from user

segments = []
lenghtOfSegments = []
segLengthPair = []

checkAnotherIp = True

while checkAnotherIp:
    ipAddres = input("\nplease enter the IP Address: ").strip()
    if ipAddres == '':
        print("Please enter an IP Address\n")
    else:
        ipSegemnts = ipAddres.split('.')
        print("There are {0} segments in the address {1}".format(len(ipSegemnts), ipAddres))

        for n in range(0, len(ipSegemnts)):
            if (n == 0) and (ipSegemnts[n] == ''):
                continue
            segments.append(ipSegemnts[n])
            lenghtOfSegments.append(len(ipSegemnts[n]))
        else:
            segLengthPair = zip(segments, lenghtOfSegments)

        print("Segment\t\t\tLength of segment")
        for sgmnt, lngth in segLengthPair:
            print(sgmnt + "\t\t\t\t" + str(lngth))

    goAgain = input("Do you want to check another IP Address? (y/n): ")
    if goAgain == 'n' or goAgain == 'N':
        checkAnotherIp = False
    segments = []
    lenghtOfSegments = []
    segLengthPair = []

print('\n')
print("Program finished")
