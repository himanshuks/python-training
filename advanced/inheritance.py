# Inheritance in action
class Employee:
    company = "Google"

    def display(self):
        print("Parent class")


# Station inherits the Employee class
class Station(Employee):
    company = "Google"

    def display(self):
        super().display()
        print("Middle class")


# If multiple inheritance is done, priority will be given to the First Class mentioned


class Programmer(Station):
    def display(self):
        # super keyword is used to call parent function IF it has same name
        super().display()
        print("Child class")


e = Employee()
p = Programmer()

# p.show()
# p.display()

# For class Programmer, Station's Display function was called then Programmer's Display
z = Programmer()
z.display()
