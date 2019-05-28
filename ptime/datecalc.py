import time

print(time.gmtime(0))

# ##this is UTC or GMT
# print(time.gmtime())

# ## this is the DST or BST-British Summer Time
# print(time.localtime(time.time()))

# print(time.time())

# ##formats the time in the form DayName, MonthName Day H:M:S Year
# print(time.asctime(time.gmtime(time.time())))

# print(time.asctime(time.localtime(time.time())))

# print(time.process_time())

time_here = time.localtime()

# accessing time elements from a name tuple of struct_tuple of the localtime() returned value
print(time_here)
print("Year:", time_here[0], time_here.tm_year)
print("Month:", time_here[1], time_here.tm_mon)
print("Month:", time_here[2], time_here.tm_mday)

# formting time as string or human readable form
print(time.strftime("%A %d %B, %Y", time.localtime()))
print(time.strftime("%x", time.localtime()))
