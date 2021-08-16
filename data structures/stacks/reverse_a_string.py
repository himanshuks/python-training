# Reversing the String using DEQUE

from collections import deque

# STACK functionality is created using class
# It has multiple functions which includes ADD, REMOVE, CHECK LAST ELEMENT
# Get length of STACK and check is it's empty


class Stack:
    def __init__(self):
        self.container = deque()

    def add_item(self, data):
        return self.container.append(data)

    def remove_item(self):
        return self.container.pop()

    def see_last_element(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def get_length(self):
        return len(self.container)


s = Stack()
s.add_item("himanshu")
s.add_item("nikhil")

print(s.get_length())
print(s.see_last_element())


# To reverse the string
# Create a stack and push each character of string
# Then pop out the stack and create string by appending popped element


def reverse_string(str):
    rev = Stack()

    for ch in str:
        rev.add_item(ch)

    revStr = " "

    while rev.get_length() != 0:
        revStr += rev.remove_item()

    return revStr


x = reverse_string("Hello, world! Himanshu is here...")
print(x)
