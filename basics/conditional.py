# If conditions with IF-ELSE-IF ladder
a = 15

if a > 3:
    print("A is greater than 3")
elif a > 17:
    print("A is greater than 17")
elif a > 5:
    print("A is greater than 5")
elif a > 10:
    print("A is greater than 10")
else:
    print("A is smaller")

print("IF ELSE IF ladder is over...")


# Only IF ladder
if a > 3:
    print("A is greater than 3")

if a > 17:
    print("A is greater than 17")

if a > 5:
    print("A is greater than 5")

if a > 10:
    print("A is greater than 10")
else:
    print("A is smaller")


age = int(input("Enter you age: "))
if age > 18:
    print("You are adult now")
else:
    print("You are still a kid")


# else is optional in IF-ELSE-IF ladder
z = 5
if z == 7:
    print("Good")
elif z > 19:
    print("Boy")


# Spam words check
sample_text = input("Enter the text: \n")
isSpam = False
if "make a lot of money" in sample_text:
    isSpam = True
elif "buy now" in sample_text:
    isSpam = True
elif "click now" in sample_text:
    isSpam = True
else:
    isSpam = False

if isSpam:
    print("This is spam text")
else:
    print("This is not a spam text")


# Check username length
name = input("Enter your username: ")
if len(name) < 10:
    print("Username needs at least 10 characters")
else:
    print("Username is perfect")
