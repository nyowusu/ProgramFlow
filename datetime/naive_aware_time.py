import datetime
import pytz

local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

print("Naive local time {}".format(local_time))
print("Naive UTC time {}".format(utc_time))

# converting to aware time.
# changes it to the current localtime zone
aware_local_time = pytz.utc.localize(local_time).astimezone()
aware_utc_time = pytz.utc.localize(utc_time)

print("Aware local time {}, time zone {}".format(
    aware_local_time, aware_local_time.tzinfo))
print("Aware UTC time {}, time zone {}".format(
    aware_utc_time, aware_utc_time.tzinfo))
