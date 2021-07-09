# Working with getter and setter
class Employee:
    company = "Indian Oil"
    basic = 5000
    bonus = 1000

    @property  # used to make function appear and used as PROPERTY
    def salary(self):
        return self.bonus + self.basic

    @salary.setter  # used to set values of class for such PROPERTY function
    def salary(self, val):
        self.bonus = val - self.basic


e = Employee()

# Instead of calling the function, we are using it as normal variable
print(e.salary)

# Assigning value to this function
# we get 2000 as result, as val=7000 and basic=5000
e.salary = 7000
print(e.bonus)
