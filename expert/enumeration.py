# ENUMERATE - To iterate while tracking index of element
list = [3, 8, 5, False, 9, "Himanshu", 22.7]

for item in list:
    print(item)


# We can use enumerate to iterate over list using counter track
# X,Y can be of any name but first parameter will be index and second parameter will be item itself
for index, item in enumerate(list):
    print(f"The item at {index} index is {item}")


for i, j in enumerate(list):
    print(f"Item at index {i} is {j}")
