# Reading log file
# Read till it gets contents and return line number
content = True
i = 1
with open("d:\\visual studio\\python practice\\advanced\\log.txt", "r") as f:
    while content:
        content = f.readline()
        if "python" in content:
            print(content)
            print(f"The word 'python' is found at line {i}")
        i += 1


# We can use READLINES to get line by line as LIST from a file
# In this way, we don't have to use WHILE loop
with open("d:\\visual studio\\python practice\\advanced\\log.txt", "r") as f:
    for line in f.readlines():
        print(line)


with open("d:\\visual studio\\python practice\\advanced\\sample.txt", "r") as f:
    content = f.readlines()
    print(content, "\n")
    print(list(reversed(content)))  # reversed can be used to get list in reverse order
