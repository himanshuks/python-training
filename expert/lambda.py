def display(a):
    return a + 10


print(display(7))

# lambda functions are used to create single line functions
# FUNCTION NAME = lambda PARAMETER_LIST : RETURN_EXPRESSION

square = lambda x: x * x

sum = lambda x, y, z: x + y + z

print(square(3))
print(sum(5, 8, 2))
