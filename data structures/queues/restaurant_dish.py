# Threading is used in below function to provide delay in taking and making orders in a restaurant

from collections import deque
import time
import threading


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, data):
        return self.buffer.appendleft(data)

    def dequeue(self):
        return self.buffer.pop()


food = Queue()

# Function for placing orders
def place_orders(orders):
    for dish in orders:
        print("Placing order :", dish)
        food.enqueue(dish)

        # Gap of 0.5 seconds between each dish order
        time.sleep(0.2)


# Function for serving orders
def serve_orders():
    time.sleep(1)
    for dish in orders:
        x = food.dequeue()
        print("Now serving :", x)

        # Gap of 3 seconds between each served dish
        time.sleep(2)


orders = [
    "pizza",
    "samosa",
    "pasta",
    "biryani",
    "burger",
    "sandwich",
    "omelette",
    "milkshake",
]
print("Restaurant started...")

# Two parallel threads will run
# One will place order, other will serve order

th1 = threading.Thread(target=place_orders, args=(orders,))
th2 = threading.Thread(target=serve_orders, args=())

th1.start()
th2.start()

# JOIN - when used will wait child thread to get complete and wait to join in main thread

th1.join()
th2.join()

print("All order completed...")
