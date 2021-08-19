#  SINGLE NODE ELEMENT


class Node:

    # Constructor to set data and next node in list
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# LINKED LIST ELEMENT
class LinkedList:

    # Constructor to create HEAD pointer
    def __init__(self):
        self.head = None

    # Display list by iterating each node present in list
    def print_list(self):
        if self.head is None:
            print("The linked list is empty")
            return

        itr = self.head  # Iterator created
        listString = "START"

        while itr:
            listString += " -> " + str(itr.data)
            itr = itr.next

        print(listString)

    # Insert at START -> Make node and assign to header
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    # Insert at END -> Make node and assign to header
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    # Insert at particular INDEX
    def insert_at_index(self, index_of_element, element):

        if index_of_element < 0 or index_of_element >= self.get_length():
            raise Exception("Invalid index provided")

        if index_of_element == 0:
            newNode = Node(element, self.head)
            self.head = newNode

            # You can also use defined function
            # self.insert_at_begining(element)

        count = 0
        itr = self.head
        while itr:
            if count == index_of_element - 1:
                itr.next = Node(element, itr.next)
                break

            itr = itr.next
            count += 1

    # Flush and insert list with new values of node
    def insert_new_values(self, data_from_list):
        self.head = None

        for item in data_from_list:
            self.insert_at_end(item)

    # Get length of the linked list
    def get_length(self):
        count = 0

        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    # Remove element at particular node
    def remove_element(self, element_at_node):

        if element_at_node < 0 or element_at_node >= self.get_length():
            raise Exception("Invalid index provided")

        if element_at_node == 0:
            self.head = self.head.next

        count = 0
        itr = self.head
        while itr:
            if count == element_at_node - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    # Insert by VALUE
    def insert_by_value(self, data_after, data_to_insert):

        # Will ONLY check if item to be inserted is at START
        if self.head.data == data_after:
            newNode = Node(data_to_insert, self.head.next)
            self.head.next = newNode
            return

        # Apart from START, below code will work
        itr = self.head
        while itr:
            if itr.data == data_after:
                newNode = Node(data_to_insert, itr.next)
                itr.next = newNode
                break

            itr = itr.next

    # Remove by VALUE
    def remove_by_value(self, data_to_remove):

        # Will ONLY check if item to be inserted is at START
        if self.head.data == data_to_remove:
            self.head = self.head.next
            return

        # Apart from START, below code will work
        count = 0
        itr = self.head
        while itr.next:
            if itr.next.data == data_to_remove:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1


myList = LinkedList()
myList.print_list()

myList.insert_at_begining(10)
myList.insert_at_begining(30)
myList.insert_at_end(90)
myList.insert_at_begining(70)

myList.print_list()

myList.insert_at_end(20)
myList.insert_at_begining(50)
myList.insert_at_end(100)

myList.print_list()

myList.insert_new_values(
    ["mango", "banana", "apple", "guava", "pineapple", "cheery", "melon"]
)
myList.print_list()

print("Length of the linked list is", myList.get_length())
print("Item at index 3 is removed from node")
myList.remove_element(3)
myList.print_list()

myList.insert_at_index(0, "avocado")
myList.print_list()
myList.insert_at_index(2, "jackfruit")
myList.print_list()

myList.insert_by_value("cheery", "kiwi")
myList.print_list()

myList.insert_by_value("avocado", "pear")
myList.print_list()

myList.remove_by_value("avocado")
myList.print_list()
