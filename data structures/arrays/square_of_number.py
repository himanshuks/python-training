# TO GET LIST OF SQUARED NUMBER WITH MAX NUMBER INPUT FROM USER


def squareOfNumber(num):
    squared_numbers = []
    for i in range(1, num + 1):
        squared_numbers.append(i * i)
    return squared_numbers


x = int(input("Enter the number for Square List: "))
print(squareOfNumber(x))
