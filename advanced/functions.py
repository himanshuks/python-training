# Default parameters can be passed using (=)
def greetMe(name="himanshu"):
    print("Good Morning, " + name)


x = input("Enter name: ")
greetMe(x)
greetMe()

# Recursive function


def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num - 1)


print(factorial(8))


# Careful when joining string with integer
zo = 5
print(
    "Check string concatenation using + operator" + str(zo) + "post integer value."
)  # use + to concatenate
print(
    "Check string concatenation using + operator", zo, "post integer value."
)  # use , for joining
# use f function for {} evaluation
print(f"Check string concatenation using + operator {zo} post integer value.")


# Use end="" to restrict new line coming automatically - default is \n
print("hello", end=" ")
print("world", end=" ")
print("himanshu", end=" ")
print("here", end=" ")


def sumNatural(num):
    if num == 0:
        return 0
    else:
        return num + sumNatural(num - 1)


x = int(input("\nEnter number: "))
print(f"The sum of first {x} natural number is {sumNatural(x)}.")
