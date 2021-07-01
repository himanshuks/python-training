# While loop in action
i = 1
print("Table of 5 :")
while i < 11:
    print("5 X " + str(i) + " = " + str(i * 5))
    i = i + 1

print("Table finished")


# While loop for list traversal
fruits = ["banana", "watermelon", "pineapple", "apple", "mango", "cherry"]
x = 0
while x < len(fruits):
    print(fruits[x])
    x = x + 1

print("Fruits finished using while loop")


# For loop for list traversal
for item in fruits:
    print(item)

print("Fruits finished using for loop")


# Range function to create list of numbers
# Parameters are START, END, SKIP SIZE
# Size is 0 by default
# End is mandatory to give
# Step size is 1 by default

for x in range(1, 9):
    print(x)

# Using step size
print("using step size")
for x in range(1, 9, 2):
    print(x)


for y in range(5):
    print(y)
else:
    print("For loop got closed")


for i in range(20, 30):
    if i == 25:
        continue
    print(i)


# Print table
print("General table is below")
num = int(input("Enter the number: "))
for x in range(1, 11):
    print(f"{num} X {x} = {num*x}")


# Find factorial of number
print("Factorial Code")
num2 = int(input("Enter the number: "))
fact = 1
for z in range(1, num2 + 1):
    fact = fact * z
print(f"The factorial of {num2} is {fact}.")
