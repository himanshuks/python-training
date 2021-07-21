# Import below modules
# TIME - used for wait function, current time etc
# THREADING - used for multi thread workers

import time
import threading


def find_square(num):
    print("Calculate square of numbers:")

    for x in num:

        # Sleep - provides delay (same like timeOut)
        time.sleep(0.5)
        print(f"Square of {x} is {x*x}\n")


def find_cube(num):
    print("Calculate cube of numbers:")

    for x in num:
        time.sleep(0.5)
        print(f"Cube of {x} is {x*x*x}\n")


t = time.time()

arr = [2, 3, 5, 7, 9]

# Create an instance with TARGET of worker like function
# ARGS as parameters in TUPLE format

th1 = threading.Thread(target=find_square, args=(arr,))
th2 = threading.Thread(target=find_cube, args=(arr,))

# START is used to execute thread simultaneously
th1.start()
th2.start()

# JOIN will wait till the threads are completed, else rest of the code will get executed
# It will join the main thread once it gets completed
th1.join()
th2.join()

# Below code execution is held till threads are completed -> through JOIN()
print("Completed in", time.time() - t)
