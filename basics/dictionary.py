# Dictionary are mutable, unorganized and indexed
myDict = {
    "name": "himanshu",
    "marks": 45,
    "arr": [2, 5, 7, 1, 3],
    "dicttwo": {"age": 21, "tuple": (5, 1, 7, 2, 3)},
}

print(myDict)

print(myDict["marks"])
print(myDict["name"])
print(myDict["dicttwo"]["tuple"])

# Dictionary methods
print(myDict.keys())  # to get keys
print(list(myDict.keys()))

print(myDict.values())  # to get values
print(list(myDict.values()))

print(myDict.items())  # to get key value pair as tuple

# UPDATE appends the new data on dictionary
# If KEY is present in dictionary, then that value gets updated
second = {"golu": "friend", "bitu": "friend", "raju": "friend"}
print(second)
myDict.update(second)
print(myDict)


# Both fetch value for the key, only difference is [] will give syntax error and GET as none
print(myDict.get("name"))
print(myDict.get("name2"))
# print(myDict["name2"])
