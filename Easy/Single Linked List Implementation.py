

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
    
    def insert(self, newNode):
        if self.head is None:
            self.head = newNode
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = newNode

    def insert_at_beginning(self, newNode):
        if self.head is None:
            print("List has no items")
            return
        newNode.next = self.head
        self.head = newNode

    def insert_item_before_another_item(self, x, newNode):
        if self.head is None:
            print("list has no items")
            return
        if x == self.head.data:
            newNode.next = self.head
            self.head = newNode
            return
        n = self.head
        print(n.next)
        while n.next is not None:
            if n.next.data == x:
                break
            n = n.next
        if n.next is None:
            print("item not found in the list")
        else:
            newNode.next = n.next
            n.next = newNode

    def insert_at_index(self, index, newNode):
        if index == 1:
            newNode.next = self.head
            self.head = newNode
        n = self.head       
        
    def printList(self):
        if self.head is None:
            print("list has no element")
            return
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.next            

firstNode = Node("John")
linkedList = LinkedList()
linkedList.insert(firstNode)
secondNode = Node("Ben")
linkedList.insert(secondNode)
thirdNode = Node("Matthew")
linkedList.insert(thirdNode)
fourthNode = Node("Mak")
linkedList.insert_at_beginning(fourthNode)
fifthNode = Node("Bruce")
linkedList.insert_item_before_another_item("John", fifthNode)
sixthNode = Node("Jack")
linkedList.insert_at_index(3,sixthNode)
linkedList.printList()
