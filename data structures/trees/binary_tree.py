# Binary Tree has only 2 child nodes, LEFT and RIGHT
class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # Adding a CHILD node
    def add_child(self, data):

        # Because duplicates are not allowed
        if data == self.data:
            return

        # When DATA is less than current NODE, call recursively again
        if data < self.data:

            # Current node is LEAF node, create new NODE else repeat
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)

        # When DATA is greater than current NODE, call recursively again
        else:

            # Current node is LEAF node, create new NODE else repeat
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    # In-order traversal - LDR (Left, Data, Right)
    # This sorts the tree in ascending order
    # Order of condition is necessary to follow in-order traversal
    def in_order_traversal(self):
        elements = []

        # Repeat on LEFT node till it is present
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        # Repeat on RIGHT node till it is present
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    # Searching the element
    def search_element(self, find):

        # When current element gets matched
        if find == self.data:
            return True

        # Repeat on LEFT node till it is present
        # Return FALSE is node reached end
        if find < self.data:
            if self.left:
                return self.left.search_element(find)
            else:
                return False

        # Repeat on RIGHT node till it is present
        # Return FALSE is node reached end
        if find > self.data:
            if self.right:
                return self.right.search_element(find)
            else:
                return False


# Create a binary tree with LIST of numbers
def build_binary_tree(elements):

    # Created ROOT element
    root = BinarySearchTreeNode(elements[0])

    # Add NODES for each element in LIST
    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


numbers = [17, 5, 22, 12, 78, 34, 56, 2, 9]
number_tree = build_binary_tree(numbers)

print(number_tree.in_order_traversal())
print(number_tree.search_element(12))
