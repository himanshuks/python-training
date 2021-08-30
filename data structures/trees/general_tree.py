# TREE data structure will have connected NODES
class TreeNode:

    # Constructor will DATA, list of children(NODE) and parent(NODE)
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    # When adding new NODE, append CHILD in LIST and connect CHILD's PARENT to NODE
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    # Get number of levels
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    # Print the TREE in GUI
    def print_tree(self):

        # These will add spaces and dashes
        spaces = " " * self.get_level() * 5

        # Attach PREFIX only when PARENT is present
        prefix = spaces + "|---" if self.parent else ""
        print(prefix + self.data)

        # Till CHILDREN are present, for each child in LIST, do recursion
        if len(self.children) > 0:
            for child in self.children:
                child.print_tree()


def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptops")
    smartphone = TreeNode("SmartPhones")
    tv = TreeNode("Television")

    laptop.add_child(TreeNode("Mac Pro"))
    laptop.add_child(TreeNode("Thinkpad"))
    laptop.add_child(TreeNode("Inspiron"))

    smartphone.add_child(TreeNode("OnePlus"))
    smartphone.add_child(TreeNode("RealMe"))
    smartphone.add_child(TreeNode("Motorola"))

    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(smartphone)
    root.add_child(tv)

    return root


x = build_product_tree()
x.print_tree()
