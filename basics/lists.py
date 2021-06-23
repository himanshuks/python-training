# Create a list using []
my_list = [1, 5, 3, 9, 4, 12]
print(my_list)

# Access element using index
print(my_list[2])

# Update element using index
my_list[1] = 10
print(my_list)

# List of different datatypes can be created
glo_list = [20, "himanshu", True, 3.17]
print(glo_list)

# List slicing
friends = ["himanshu", "monu", "tanya", "naveen", "jyoti"]
print(friends[0:3])
print(friends[-4:-1])

# List methods
arr = [23, 78, 33, 11, 65, 45, 98, 17]
print(arr)

arr.sort()  # ascending order
print(arr)

arr.reverse()  # descending order
print(arr)

arr.append(50)  # add at end
print(arr)

arr.pop(2)  # remove by index
print(arr)

arr.remove(11)  # remove by value
print(arr)

arr.insert(1, 69)  # insert at X index with Y element
print(arr)
