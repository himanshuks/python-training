# Working with TRY-CATCH blocks
# If code is successful, it gets executed
# If not, except block gets executed
try:
    a = int(input("Enter a number: "))
    c = 1 / a
    print(f"Division of 1/{a} is {c}")

    # Can provide specific exception error like value error
except ValueError:
    print("Please enter only numbers")

    # Can provide specific exception error like zero division error
except ZeroDivisionError:
    print("Do check you are not dividing by zero")
except:
    print("Different error occurred")
    exit()
else:
    print(
        "ELSE block gets executed only when TRY is successful with capturing any error"
    )

# You can't stop finally block to get executed irrespective of whatver you do in EXCEPT block
finally:
    print("FINALLY block gets executed irrespective of error caught OR program exits")


def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("Custom error message by Himanshu")


a = increment(5)
print(a)
