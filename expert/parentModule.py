# Parent File
def greet(name):
    print(f"Good morning, {name}")


# When used if __name__ == "__main__":
# Contents under it will get executed only if current file is executed
# If file/content is imported as module in different file then contents will not get executed from other file
print("Based on current fileName : ", __name__)
if __name__ == "__main__":
    a = input("Enter name: ")
    greet(a)
