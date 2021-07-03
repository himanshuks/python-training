# Reading file contents

import os

# Get current directory with below function
print(os.listdir())

# Default mode is r
# You can use read function only once, multiple read will be ignored
f = open("d:\\visual studio\\python practice\\advanced\\sample.txt", "r")
# data = f.read()
# data = f.read(50)       # get first 50 characters
# print(data)

data2 = f.readline()  # read the first line
print(data2)
f.close()

f = open("d:\\visual studio\\python practice\\advanced\\check.txt", "r")
data = f.read()
print(data)
f.close()

# Different modes of operation are
# for read - r
# for write - w
# for append - a
# for both - +

f = open("d:\\visual studio\\python practice\\advanced\\another.txt", "w")
f.write("Dynamic file created using python")
f.close()

f = open("d:\\visual studio\\python practice\\advanced\\another.txt", "a")
f.write("\nWe are appending this text at the bottom of the file")
f.close()

# for reading binary files, use operator - rb
# by default operator is rt (for text files)

# Using WITH keyword, no need to close the file explicitly
with open("d:\\visual studio\\python practice\\advanced\\another.txt", "a") as f:
    f.write("\nMy name is himanshu")
