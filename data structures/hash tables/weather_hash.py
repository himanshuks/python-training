arr = []

# First read the file
with open(
    "D:\\visual studio\\python practice\\data structures\\hash tables\\nyc_weather.csv"
) as f:

    # Get one line at a time
    for line in f:

        # Split the contents based on character and creates LIST
        tokens = line.split(",")
        print(f"The current token is {tokens}")
        try:
            # Get second element from LIST
            temperature = int(tokens[1])
            print("The temperature is", temperature)

            # Add it into the main ARRAY
            arr.append(temperature)
        except:
            print("Invalid temperature. This is row heading.")


print(arr)
print(f"The average temperature of 1st week is {sum(arr[0:7])/len(arr[0:7])}")
print(f"Maximum temperature in first 10 days is {max(arr[0:10])}")

dict = {}
with open(
    "D:\\visual studio\\python practice\\data structures\\hash tables\\nyc_weather.csv"
) as f:
    for line in f:
        token = line.split(",")
        print("My token is ", token)
        try:
            # Get first, second element on current token
            day = token[0]
            temp = int(token[1])
            dict[day] = temp
        except:
            print("This is first row")


print(dict)
print("Temperature on Jan 9 is", dict["Jan 9"])
print("Temperature on Jan 4 is", dict["Jan 4"])
