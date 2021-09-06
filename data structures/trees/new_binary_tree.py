class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, newData):

        if self.data == newData:
            return

        if newData < self.data:
            if self.left:
                self.left.add_child(newData)
            else:
                self.left = BinaryTreeNode(newData)

        if newData > self.data:
            if self.right:
                self.right.add_child(newData)
            else:
                self.right = BinaryTreeNode(newData)

    def search_element(self, element):

        if self.data == element:
            return True

        if element < self.data:
            if self.left:
                return self.left.search_element(element)
            else:
                return False

        if element > self.data:
            if self.right:
                return self.right.search_element(element)
            else:
                return False

    def in_order_traversal(self):
        newList = []

        if self.left:
            newList += self.left.in_order_traversal()

        newList.append(self.data)

        if self.right:
            newList += self.right.in_order_traversal()

        return newList

    def pre_order_traversal(self):
        newList = []

        newList.append(self.data)

        if self.left:
            newList += self.left.pre_order_traversal()

        if self.right:
            newList += self.right.pre_order_traversal()

        return newList

    def post_order_traversal(self):
        newList = []

        if self.left:
            newList += self.left.post_order_traversal()

        if self.right:
            newList += self.right.post_order_traversal()

        newList.append(self.data)

        return newList

    def calculate_sum(self):
        return sum(self.in_order_traversal())

    def find_max(self):
        return max(self.in_order_traversal())

    def find_min(self):
        return min(self.in_order_traversal())

    def find_min_thorugh_nodes(self):

        if self.left:
            return self.left.find_min_thorugh_nodes()
        else:
            return self.data

    def find_max_thorugh_nodes(self):

        if self.right:
            return self.right.find_max_thorugh_nodes()
        else:
            return self.data


def create_new_binary_tree(list):

    root = BinaryTreeNode(list[0])

    for x in range(1, len(list)):
        root.add_child(list[x])

    return root


list = [15, 12, 7, 14, 27, 20, 23, 88]
z = create_new_binary_tree(list)

print("Number list:", list)

print("Pre Order Traversal", z.pre_order_traversal())
print("In Order Traversal", z.in_order_traversal())
print("Post Order Traversal", z.post_order_traversal())

print("Calculating sum of all elements:", z.calculate_sum())
print("Max number present TREE List:", z.find_max())
print("Min number present TREE List:", z.find_min())

print("Min number using traversal:", z.find_min_thorugh_nodes())
print("Max number using traversal:", z.find_max_thorugh_nodes())
