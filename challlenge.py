# take input from user

segments = []
lengthOfSegments = []
segLengthPair = []

checkAnotherIp = True

while checkAnotherIp:
    ipAddress = input("\nplease enter the IP Address: ").strip()
    if ipAddress == '':
        print("Please enter an IP Address\n")
    else:
        ipSegments = ipAddress.split('.')
        print("There are {0} segments in the address {1}".format(len(ipSegments), ipAddress))

        for n in range(0, len(ipSegments)):
            if (n == 0) and (ipSegments[n] == ''):
                continue
            segments.append(ipSegments[n])
            lengthOfSegments.append(len(ipSegments[n]))
        else:
            segLengthPair = zip(segments, lengthOfSegments)

        print("Segment\t\t\tLength of segment")
        for segment, length in segLengthPair:
            print(segment + "\t\t\t\t" + str(length))

    goAgain = input("Do you want to check another IP Address? (y/n): ")
    if goAgain == 'n' or goAgain == 'N':
        checkAnotherIp = False
    segments = []
    lengthOfSegments = []
    segLengthPair = []

print('\n')
print("Program finished")
