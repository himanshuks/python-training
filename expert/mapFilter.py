# MAP and FILTER functions

myList = [2, 5, 7, 4, 9]
newList = []


def square(num):
    return num * num


# METHOD 1
# To implement a function on list

for i in myList:
    newList.append(square(i))

print(newList)


# METHOD 2
# Using MAP function

print(map(square, myList))  # return MAP object

print(list(map(square, myList)))  # typecast into LIST to see the contents

secondList = [
    27,
    44,
    4,
    83,
    31,
    63,
    71,
    74,
    54,
    73,
    55,
    6,
    10,
    23,
    4,
    13,
    24,
    54,
    14,
    41,
    87,
]


def num_greater_50(num):
    if num > 50:
        return True
    else:
        return False


# Filter function can be used to filter items based on function
print(list(filter(num_greater_50, secondList)))


# Reduce apply rolling computation on list items in sequential manner
# Import it from FUNCTOOLS module
from functools import reduce

x = [1, 5, 8, 3, 9, 7]

# Take 2 numbers and return their multiplication
multi = lambda x, y: x * y

# Reduce will apply MULTI function on each element from X
# And repeat the process for next element with previous result
var = reduce(multi, x)
print(var)
