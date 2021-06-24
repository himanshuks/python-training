# Sets can be created using {}
my_set = {3, 6, 1, 8, 3, 2, 6, 5}
print(my_set)

# Set contain only unique items
# Set are unordered and un-indexed
a = {}
print(type(a))

b = set()
print(type(b))

b.add(4)
b.add(7)
b.add(7)
b.add(5)
print(b)

# b.add([9, 8, 7])      # list can't be added into set because list is hashable and it contains duplicates
b.add((11, 22, 33))  # tuple can be added into set
# b.add({4: 888})       # dictionary can't be added too
print(b)

print(len(b))  # gives the length of set

b.remove(5)  # removes the element from set
# b.remove(15)          # throw error if that element is removed which is not present
print(b)

b.pop()  # can delete any random element once
print(b)

# other function include CLEAR, UNION, INTERSECTION

check_set = set()
check_set.add(20)
check_set.add("20")
check_set.add(20.00)

print(check_set)

# length will come as 2 because both 20 and 20.0 will be treated as 20 while evaluating
print(len(check_set))
