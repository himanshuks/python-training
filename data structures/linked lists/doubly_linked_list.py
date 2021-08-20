# Implementation of Doubly Linked List


class DoubleNode:

    # Constructor with 3 parameters to create node
    def __init__(self, data=None, previous=None, next=None):
        self.data = data
        self.previous = previous
        self.next = next


class DoublyLinkedList:

    # Constructor to create HEAD pointer
    def __init__(self):
        self.head = None

    # Retrieve length of the DLL
    def get_length(self):
        count = 0
        itr = self.head

        # This will reach till last NODE
        while itr:
            count += 1
            itr = itr.next

        return count

    # Get last node of DLL
    def get_last_node(self):
        itr = self.head

        # Till last iterator NEXT is None
        # So we will reach at last NODE
        while itr.next:
            itr = itr.next

        return itr

    # Iterate DLL in forward direction
    def print_doubly_linked_list_forward(self):
        if self.head is None:
            print("Doubly linked list is empty")
            return

        itr = self.head
        dllStr = "START"

        # Till NEXT node is present in current ITR
        while itr:
            dllStr += " <--> " + str(itr.data)
            itr = itr.next

        print(f"Forward DLL\n {dllStr} <--> END")

    # Iterate DLL in backward direction
    def print_doubly_linked_list_backward(self):
        if self.head is None:
            print("Doubly linked list is empty")

        itr = self.get_last_node()
        dllStr = "END"
        while itr:
            dllStr += " <--> " + str(itr.data)
            itr = itr.previous

        print(f"Backward DLL\n {dllStr} <--> START")

    # Insert element at START
    def insert_at_begining(self, data):

        # When list is empty, simply assign node to HEAD
        if self.head is None:
            newNode = DoubleNode(data, None, self.head)
            self.head = newNode

        # Create node -> Point to HEAD's PREVIOUS -> Assign node to HEAD
        else:
            newNode = DoubleNode(data, None, self.head)
            self.head.previous = newNode
            self.head = newNode

    # Insert element at END
    def insert_at_end(self, data):
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = DoubleNode(data, itr, None)

    # Insert at INDEX
    def insert_at_index(self, index, data):
        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head

        while itr:
            if count == index - 1:

                # Create NODE with next pointing to current ITR's NEXT
                # and previous pointer to current ITR
                newNode = DoubleNode(data, itr, itr.next)

                # Assign new NODE's NEXT N0DE previous pointer to new NODE
                if newNode.next:
                    newNode.next.previous = newNode

                # Make current ITR's NEXT pointer to new NODE
                itr.next = newNode
                break

            count += 1
            itr = itr.next

    # Remove based on INDEX
    def remove_at_index(self, index):

        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index provided")

        if index == 0:
            self.head = self.head.next
            self.head.previous = None
            return

        count = 0
        itr = self.head

        while itr.next:
            if count == index - 1:
                itr.previous = itr.next.previous
                itr.next = itr.next.next
                break

            count += 1
            itr = itr.next


myDLL = DoublyLinkedList()

myDLL.insert_at_begining(5)
myDLL.insert_at_begining(7)
myDLL.insert_at_begining(1)
myDLL.print_doubly_linked_list_forward()

myDLL.insert_at_end(2)
myDLL.insert_at_end(9)
myDLL.print_doubly_linked_list_forward()

print("DLL length", myDLL.get_length())
myDLL.print_doubly_linked_list_backward()

myDLL.insert_at_index(0, 20)
myDLL.insert_at_index(0, 70)
myDLL.print_doubly_linked_list_forward()

myDLL.insert_at_index(4, 100)
myDLL.insert_at_index(6, 500)
myDLL.print_doubly_linked_list_forward()

myDLL.remove_at_index(5)
myDLL.print_doubly_linked_list_forward()
