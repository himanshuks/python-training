# Dependent File

import parentModule

parentModule.greet("Himanshu")

a = 50


def showMe():

    # To call global value inside local scope for change
    global a
    print(f"A can be used as global value")

    # This will update value of A globally
    a = 60
    print(f"The value of A in local scope is {a}")


showMe()

# If global keyword is not inside local scope, GLOBAL value will get displayed

print(f"The value of A global scope is {a}")
