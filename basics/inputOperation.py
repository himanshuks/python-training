# Take multiple inputs from single line using SPLIT function

z = [
    int(x) for x in input("Enter numbers separated by space to create list : ").split()
]

print(z)

sum = 0
for val in z:
    sum += val

print("The sum of all elements :", sum)
