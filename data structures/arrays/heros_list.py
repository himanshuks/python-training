# PERFORM BELOW OPERATIONS ON LIST

"""
1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
"""

heros = ["spider man", "thor", "hulk", "iron man", "captain america"]

# LEN - returns the length of list
print("The length is", len(heros))

heros.append("black panther")
print("New list is", heros)

# REMOVE - delete the element
# INSERT - insert element at fixed index
heros.remove("black panther")
heros.insert(3, "black panther")
print("New list after changes is", heros)

# Here 3rd index item is not included, so only THOR and HULK will get replaced single DOCTOR STRANGE
heros[1:3] = ["doctor strange"]
print("Adding doctor is list", heros)

# SORT - arrange the item elements in increasing order
heros.sort()
print("Sorted list is ", heros)
