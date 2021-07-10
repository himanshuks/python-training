# Class declaration
class RailwayReservation:
    def displayInfo(self):
        print(f"The name is {self.name}")
        print(f"The train is {self.train}")


himanshuApp = RailwayReservation()
himanshuApp.name = "Himanshu"
himanshuApp.train = "Rajdhani Express"
himanshuApp.displayInfo()


class Company:
    name = "Google"  # Class Attribute
    salary = 100


himanshu = Company()
mayank = Company()
print(himanshu.name)
print(mayank.name)

Company.name = "Flipkart"
print(himanshu.name)
print(mayank.name)

himanshu.salary = 400  # Instance attribute

# If present instance attribute value will be used
print(himanshu.salary)
# If not present , object attribute value will be taken
print(mayank.salary)


class Employee:
    company = "Amazon"

    def getSalary(self):
        print(f"The salary is {self.salary}")


hks = Employee()
hks.salary = 50000
hks.getSalary()  # This gets converted into -> Employee.getSalary(hks)
# So we provide SELF argument in function to access attributes
