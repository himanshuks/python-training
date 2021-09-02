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

    def in_order_traversal(self):
        newList = []

        if self.left:
            newList += self.left.in_order_traversal()

        newList.append(self.data)

        if self.right:
            newList += self.right.in_order_traversal()

        return newList

    def find_max(self):
        return max(self.in_order_traversal())

    def find_min(self):
        return min(self.in_order_traversal())

    # Below function will delete the NODE
    def delete_node(self, val):

        # Search for current NODE
        if val < self.data:

            # Repeat till you get LEFT node
            if self.left:
                self.left = self.left.delete_node(val)

        elif val > self.data:

            # Repeat till you get RIGHT node
            if self.right:
                self.right = self.right.delete_node(val)

        # When it get match, check for NODES
        else:

            # Check if it's LEAF node, NO CHILDREN
            if self.left is None and self.right is None:
                return None

            # If have only ONE CHILD
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            # First find minimum value in RIGHT tree
            # Make current NODE to that value
            # Shift RIGHT tree by one unit
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete_node(min_val)

        return self


def create_new_binary_tree(list):

    root = BinaryTreeNode(list[0])

    for x in range(1, len(list)):
        root.add_child(list[x])

    return root


list = [17, 4, 1, 20, 9, 23, 18, 34]
z = create_new_binary_tree(list)

print("Before:", z.in_order_traversal())
z.delete_node(23)
print("After:", z.in_order_traversal())
