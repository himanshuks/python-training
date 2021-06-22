# First python code
# Below is Multi-line comments
"""
Author: Himanshu
"""

msg = "Hello world, Himanshu is here..."
print(msg)

print(
    """Zerodha Broking Limited is an Indian financial services company, 
that offers retail and institutional broking, currencies and commodities 
trading, mutual funds, and bonds."""
)

a = 5
b = "singh"

# Use type function to get the datatype of the variable
print(type(a))
print(type(b))

d = "7687"
c = float(d)
c += 5

print(type(c))
print(c)
print(type(d))

# Input is used to take value from user
x = input("Enter the number: ")
print(x)

sample_string = "today is wednesday "
sample_two = "ROHAN"
print(sample_string + sample_two)

# We can use [] to access characters like array index
# [X:Y] -> between first and last index (last excluded)
# [-1] -> points to last index
print(sample_two[0:3])
print(sample_two[-1])
print(sample_two[-4:-1])
