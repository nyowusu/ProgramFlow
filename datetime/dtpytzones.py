import pytz
import datetime

country = 'Europe/London'
# this creates a timezone object to make the datetime object aware
tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)

print("The time in {} is {}".format(country, local_time.timetz()))
print("UTC is {}".format(datetime.datetime.utcnow().timetz()))

# # prints all the timezones
# for x in pytz.all_timezones:
#     print(x)

# # gets the country_name key-value
# for x in sorted(pytz.country_names):
#     print(x + ": " + pytz.country_names[x])

# # this uses the .get(x) method instead of accessing using the list notation
# for x in sorted(pytz.country_names):
#     print("{}: {}: {}".format(
#         x, pytz.country_names[x], pytz.country_timezones.get(x)))

for x in sorted(pytz.country_names):
    print("{}: {}".format(x, pytz.country_names[x]), end=": ")
    if x in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[x]):
            tz_to_display = pytz.timezone(zone)
            local_time = datetime.datetime.now(tz=tz_to_display)
            print("\t\t{}: {}".format(zone, local_time))
    else:
        print("\t\tNo time zone defined")

# always convert to UTC and work with them but only convert them to localtime when 
# displaying to the users

