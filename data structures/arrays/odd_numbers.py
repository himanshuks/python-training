# TO GET LIST OF ODD NUMBERS WITH MAX NUMBER INPUT FROM USER

num = int(input("Enter the max number: "))
oddNumList = []
for i in range(1, num + 1):
    if i % 2 != 0:
        oddNumList.append(i)

print("The list of odd numbers is", oddNumList)
