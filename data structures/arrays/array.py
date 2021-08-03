# IMPORT THE ARRAY MODULE
# IMPORTS EVERY FUNCTION FROM ARRAY MODULE

from array import *

"""
import array
myArr = array.array("i", [10, 20, 30, 40, 50])
arrayName = array.array(typecode, [Initializers])

Typecodes are:
b 	Represents signed integer of size 1 byte
B 	Represents unsigned integer of size 1 byte
c 	Represents character of size 1 byte
i 	Represents signed integer of size 2 bytes
I 	Represents unsigned integer of size 2 bytes
f 	Represents floating point of size 4 bytes
d 	Represents floating point of size 8 bytes

"""

# First parameter is the typecode provided
myArr = array("i", [10, 20, 30, 40, 50])

for x in myArr:
    print("The item is", x)


print(f"Index of 30 is", myArr.index(30))
print(f"Element at index 3 is", myArr[3])

# INSERT - to add element at an index
myArr.insert(1, 60)
print("New array after inserting 60 at index 1", myArr)

# REMOVE - delete element from array
myArr.remove(50)
print("After removing 50", myArr)

# Directly updating element at a fixed index
myArr[0] = 90
print("After updating 10 to 90", myArr)
