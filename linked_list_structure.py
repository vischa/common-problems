'''
Creating a Linked List and related common functionalities for addition and removal of nodes, 
checking for presence of nodes and returning size of Linked List nodes. 
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, item):
        self.data = item

    def setNext(self, next):
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        temp = Node(data)
        temp.setNext(self.head)
        self.head = temp

    def count(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def isPresent(self, value):
        found = False
        current = self.head
        while current != None and not found:
            if current.getData() == value:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, value):
        found = False
        previous = None
        current = self.head
        while current != None and not found:
            if current.getData() == value:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


# Driver code to test functionality
mylist = LinkedList()
# Creating a linked list
mylist.add(4)
mylist.add(5)
mylist.add(8)

print('The size of the Linked List is: {}'.format(mylist.count()))
print('Checking if value -> {} is present in the LinkedList : {}'.format(8, mylist.isPresent(value=8)))
print('Removing value {}...'.format(8))
mylist.remove(8)
print('Checking if value -> {} is present in the LinkedList : {}'.format(8, mylist.isPresent(value=8)))
print('The size of the Linked List is: {}'.format(mylist.count()))
