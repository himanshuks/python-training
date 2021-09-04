class StateTree:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent

        while p:
            level += 1
            p = p.parent

        return level

    # LEVEL is passed till where the NODES will get displayed
    def display_states(self, level):

        # CURRENT NODE length > LEVEL provided
        # Sequence for LEVEL=1 -> Global - India - Gujarat - India - Karnataka - India - Global - USA - New Jersey - USA - California - USA - Global
        if self.get_level() > level:
            return

        spaces = " " * self.get_level() * 3
        prefix = spaces + "|--" if self.parent else ""
        print(prefix + self.data)

        if self.children:
            for child in self.children:
                child.display_states(level)


def create_state_tree():

    root = StateTree("Global")

    india = StateTree("India")
    usa = StateTree("USA")
    Gujarat = StateTree("Gujarat")
    Ahmedabad = StateTree("Ahmedabad")
    Baroda = StateTree("Baroda")
    Karnataka = StateTree("Karnataka")
    Mysuru = StateTree("Mysuru")
    Bengaluru = StateTree("Bengaluru")
    Mysuru = StateTree("Mysuru")
    NewJersey = StateTree("New Jersey")
    Princeton = StateTree("Princeton")
    Trenton = StateTree("Trenton")
    California = StateTree("California")
    SanFancisco = StateTree("San Fancisco")
    MountainView = StateTree("Mountain View")
    PaloAlto = StateTree("Palo Alto")

    root.add_child(india)
    root.add_child(usa)

    india.add_child(Gujarat)
    india.add_child(Karnataka)

    usa.add_child(NewJersey)
    usa.add_child(California)

    Gujarat.add_child(Ahmedabad)
    Gujarat.add_child(Baroda)

    Karnataka.add_child(Bengaluru)
    Karnataka.add_child(Mysuru)

    NewJersey.add_child(Princeton)
    NewJersey.add_child(Trenton)

    California.add_child(SanFancisco)
    California.add_child(MountainView)
    California.add_child(PaloAlto)

    return root


x = create_state_tree()
x.display_states(1)
x.display_states(2)
x.display_states(3)
