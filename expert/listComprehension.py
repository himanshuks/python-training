import random

list = []
for i in range(21):
    list.append(random.randint(1, 100))

print(f"The random list of 20 numbers is {list}")

# Syntax - VARIABLE LOOP VARIABLE CONDITION

# Iterator name should be same
# In below we have used 'i'
evenNumber = [i for i in list if i % 2 == 0]
print(f"List of even numbers is {evenNumber}")

# Similarly we have used 'x'
numGreater = [x for x in list if x > 50]
print(f"List of numbers greater than 50 is {numGreater}")

# Creating SET from LIST
# SET doesn't contain duplicates
listForSet = [3, 1, 4, 9, 3, 7, 2, 1, 4, 2, 5]
setCom = {z for z in listForSet}
print(f"Set created from list using comprehension {setCom}")

num = int(input("Enter number for table: "))
multiplicationOfFive = [num * i for i in range(1, 11)]
print(multiplicationOfFive)
