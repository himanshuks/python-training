# Implementing stack using python LIST can be costly if the number of items are in millions

# So we use Collection.deque which is like a doubly linked list

from collections import deque

stack = deque()

# We can use DIR function to see all available methods for the FUNCTION
print(dir(stack))

stack.append("www.facebook.com")
stack.append("www.google.com")
stack.append("www.wikipedia.com")
stack.append("www.amazon.com")

print(stack)
print(stack.pop())
print(stack)
