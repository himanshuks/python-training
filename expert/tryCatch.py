# While loop executes till Q is pressed
while True:
    print("Press (q) for Quit...")
    a = input("Enter a number: ")

    if a == "q":
        break

    try:
        if int(a) > 20:
            print("Provided value is greater than 20")
        else:
            print("Provided value is less than 20")
    except Exception as e:
        print(f"Error is produced by input value : {e}")

print("Game is closed...")


itemIncart = 5
if itemIncart != 3:
    # we can raise exception anywhere if required
    raise Exception("Items in cart don't match")

assert itemIncart == 6  # asset will check if condition is TRUE or not
