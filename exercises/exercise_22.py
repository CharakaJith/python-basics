# count up timer

import time


def count(end, start=0):
    for x in range(start, end + 1):
        print(x)
        time.sleep(1)  # sleep for one second
    print("done")


# stop at 10, by default start at 0
count(10)

# stop at 10, start at 5 because of the parameter value
count(10, 5)
