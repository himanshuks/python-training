# STACK operation using LIST
# We use APPEND function to create a stack

# Works as FILO or LIFO
myStack = []

# Adding elements in Stack
myStack.append("Himanshu")
myStack.append("Tanya")
myStack.append("Monu")
myStack.append("Naveen")
myStack.append("Arti")
myStack.append("Ashutosh")

print(myStack)

# This will print only the last element
print(myStack[-1])

# This wil pop out the last element from stack
print(myStack.pop())

print(myStack)
