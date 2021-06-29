# Working with Strings
para = "hello to world, this is Himanshu. welcome to the python programming."

# Endswith returns boolean value
print(len(para))
print(para.endswith("ming."))
print(para.endswith("you"))

# Count returns number of characters
print(para.count("is"))

# Only first character
print(para.capitalize())

# find and give index of the first occurrence
print(para.find("Himanshu"))

# replace all the occurrence of the word
print(para.replace("to", "BINGO"))

paratwo = "I am a \\good boy. \nMy name is \tRahul..."
print(paratwo)

email_template = """Dear <NAME>
Good Morning, we are pleased to inform you that
You are selected <NAME> <NAME>
Regards,
Himanshu
Date : <DATE>"""

name = input("Enter name : ")
date = input("Enter date : ")

# Replace takes 2 arguments
# Then it replace the 1st argument with 2nd
# Replace all the occurrences
email_template = email_template.replace("<NAME>", name)
email_template = email_template.replace("<DATE>", date)
print(email_template)
