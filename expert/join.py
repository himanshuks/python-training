# Use JOIN to place item in between list/tuple elements
# Can be used on iterables

list = ["camera", "phone", "television", "washing machine", "refrigerator", "sofa"]

addItem = " and ".join(list)

print(addItem)
print(type(addItem))

name = "Himanshu"
company = "ABC"
city = "Delhi"
age = 25

# We use 'f' function to create dynamic string from python 3.6 onwards
sentOne = f"Hello, my name is {name} currently working in {company}. I am {age} years old living in {city}"

# Earlier we used 'format' function and passing arguments in it
# By default, order of parameters mst match with order of {}
sentTwo = "Hello, my name is {} currently working in {}. I am {} years old living in {}".format(
    name, company, age, city
)

# Place index number according to parameters to be used -> starting from ZERO
sentThree = "Hello, my name is {1} currently working in {3}. I am {2} years old living in {0}".format(
    city, name, age, company
)

print("Using f function in string -> ", sentOne)
print("using format function in string -> ", sentTwo)
print("using format function un-ordered with index in string -> ", sentThree)
