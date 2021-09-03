# TREE data structure will have connected NODES


class EmployeeTree:

    # Constructor will DATA, list of children(NODE) and parent(NODE)
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def get_length(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    # When adding new NODE, append CHILD in LIST and connect CHILD's PARENT to NODE
    def add_employee(self, child):
        child.parent = self
        self.children.append(child)

    def display_employee(self, choice):
        spaces = " " * self.get_length() * 5
        prefix = spaces + "|---" if self.parent else ""

        if choice == "name":
            print(prefix + self.name)

        elif choice == "designation":
            print(prefix + self.designation)

        elif choice == "both":
            print(prefix + self.name + " (" + self.designation + ")")

        if self.children:
            for child in self.children:
                child.display_employee(choice)


def create_employee_list():

    # Individual NODES are created
    ceo = EmployeeTree("Tanya", "CEO")
    cto = EmployeeTree("Himanshu", "CTO")
    infraHead = EmployeeTree("Monu", "Infrastructure Head")
    cloudManager = EmployeeTree("Naveen", "Cloud Manager")
    appManager = EmployeeTree("Jyoti", "App Manager")
    applicationHead = EmployeeTree("Arti", "Application Head")
    hrHead = EmployeeTree("Ashish", "HR Head")
    recruitmentManager = EmployeeTree("Ashutosh", "Recruitment Manager")
    policyManager = EmployeeTree("Tilak", "Policy Manager")

    # Nodes are added with CHILDREN
    ceo.add_employee(cto)
    ceo.add_employee(hrHead)
    cto.add_employee(infraHead)
    cto.add_employee(applicationHead)
    infraHead.add_employee(cloudManager)
    infraHead.add_employee(appManager)
    hrHead.add_employee(recruitmentManager)
    hrHead.add_employee(policyManager)

    return ceo


x = create_employee_list()
x.display_employee("name")
x.display_employee("designation")
x.display_employee("both")
