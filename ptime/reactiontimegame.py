import time
import random

input("Press enter to start")

wait_time = random.randint(1, 20)
time.sleep(wait_time)
start_time = time.time()

input("Press enter to stop")

end_time = time.time()

print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("Ended at " + time.strftime("%X", time.localtime(end_time)))

print("Your reaction time was {} seconds".format(end_time - start_time))

# to measure elapsed time regardless of the change of clock, use time.monotonic() this clock is not affected by system clock updates
# to measure elapsed time user perf_counter()
# to measure CPU process time use process_time()
