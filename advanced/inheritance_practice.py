# Inheritance in action
# Class 2D vector is created
# Class 3D vector inherits the 2D vector class
class Vector2D:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return f"The 2D vector is {self.icap}i + {self.jcap}j"


class Vector3D(Vector2D):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap = k

    def __str__(self):
        return f"The 3D vector is {self.icap}i + {self.jcap}j + {self.kcap}k"


a = Vector2D(2, 5)
b = Vector3D(3, 7, 9)

print(a)
print(b)


class Animals:
    type = "Mammal"


class Pets(Animals):
    color = "White"


# Using @staticmethod -> no need to pass SELF keyword in function
# It's a built in decorator which defines a static method
# It doesn't receive any reference argument
# They don't need state of object
# They don't require class instance creation
class Dog(Pets):
    @staticmethod
    def bark():
        print("Bow Bow ..!!!")


d = Dog()
d.bark()
