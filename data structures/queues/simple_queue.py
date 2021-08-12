# Import DEQUE module from COLLECTIONS
from collections import deque

q = deque()

# APPENDLEFT - add element on left of queue

q.appendleft(5)
q.appendleft(7)
q.appendleft(9)
q.appendleft(11)

print(q)

# APPENDLEFT - add element on right of queue

q.append(20)
q.append(80)
q.append(70)
q.append(90)
q.append(30)

print(q)

# POP - remove element on right of queue
# POPLEFT - remove element on left of queue

print(q.pop())
print(q.popleft())

# Queue class created to perform various useful functions
# Like enqueue, dequeue, size and display


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, data):
        return self.buffer.appendleft(data)

    def dequeue(self):
        return self.buffer.pop()

    def size(self):
        return len(self.buffer)

    def display(self):
        return self.buffer


mq = Queue()
mq.enqueue({"name": "Himanshu", "age": 26})
mq.enqueue({"name": "Tanya", "age": 25})
mq.enqueue({"name": "Golu", "age": 23})

print(mq.display())
