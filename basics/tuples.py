# Create a tuple using ()
setone = (1, 4, 2, 8)
print(setone)

# You can access tuple same like list
print(setone[2])

# You cannot change the values once tuple is defined (tuple are immutable)
# setone[1] = 50

settwo = ()
print(settwo)

setthree = 1  # If tuple has only one element, add comma in the end
print(setthree)

setfour = (4,)  # Like this
print(setfour)

tuple_set = (5, 2, 7, 3, 7, 2, 8, 2, 5, 1, 1, 5, 3, 2)

print(tuple_set.count(3))  # Return count of element
print(tuple_set.index(3))  # Return element at index
