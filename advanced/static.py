# Using static method in python


class Employee:
    company = "Tesla"  # This is class variable (fixed in number)

    # Initializing a constructor, called first
    def __init__(self, salary, unit):
        self.salary = (
            salary  # These two are object/instance variable (can vary in number)
        )
        self.unit = unit
        print("Employee object is created")
        print(f"Salary is {salary}")
        print(f"Unit is {unit}")

    def display(self):
        print(f"Salary is {self.salary} from display()")
        print(f"Unit is {self.unit} from display()")

    def getName(self):
        print(f"The name is {self.company}")

    # static method is used to avoid passing self argument
    # can be used for those functions which don't need attributes
    @staticmethod
    def greet():
        print("Good Morning, Team")


# We need to pass parameters in Object declaration mandatorily in constructor
# self keyword can be used to access both class and instance variable
hks = Employee(40000, "printer")
hks.getName()
hks.greet()
hks.display()
