# Internal implementation of Hash Table
# We use dictionary in python


class HashTable:

    # Create constructor with 2D array format and max length
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    # Hash function to convert key character into ASCII and take MOD of sum
    def get_hash(self, key):
        sum = 0
        for char in key:
            sum += ord(char)
        return sum % self.MAX

    # Insert element into hash
    def add_item(self, key, data):

        found = False
        position = self.get_hash(key)

        for idx, element in enumerate(self.arr[position]):
            if len(element) == 2 and element[0] == key:
                self.arr[position][idx] = (key, data)
                found = True
                break

        if not found:
            self.arr[position].append((key, data))

    # Display element from hash
    def get_item(self, key):
        position = self.get_hash(key)
        for element in self.arr[position]:
            if element[0] == key:
                return element[1]


myTable = HashTable()
myTable.add_item("himanshu", 250)
myTable.add_item("tanya", 400)
myTable.add_item("ashish", 120)

print(myTable.get_item("himanshu"))
print(myTable.get_item("ashish"))

myTable.add_item("march 6", 300)
myTable.add_item("march 17", 700)

print(myTable.arr)
