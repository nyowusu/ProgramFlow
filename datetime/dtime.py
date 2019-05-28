# use the datetime module for dates instead of time module
import time

print("The epoch on this system starts at " +
      time.strftime('%c', time.gmtime(0)))

print("The current timezone is {0} with an offset of {1}".format(
    time.tzname[0], time.timezone))
# because UK is on the GMT or UTC timezone, the time.timezone will be 0 i.e. no offset

# the daylight saving time is set for the UK hence the value of time.daylight = 1
if time.daylight != 0:
    print("\tDaylight Saving Time is in effect for this location")
    print("\tThe DST timezone is " + time.tzname[1])

print("Local time is " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print("UTC time is " + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
