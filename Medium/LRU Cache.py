#Leetcode 146. LRU Cache

#Solution1
class dll(object):
    
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity: int):
        self.head = dll(-1, -1)
        self.tail = self.head
        self.hash = {}
        self.capacity = capacity
        self.length = 0
        

    def get(self, key: int) -> int:
        if key not in self.hash:
            return -1
        node = self.hash[key]
        val = node.val
        while node.next:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node
        return val
        

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            node = self.hash[key]
            node.val = value
            while node.next:
                node.prev.next = node.next
                node.next.prev = node.prev
                self.tail.next = node
                node.prev = self.tail
                node.next = None
                self.tail = node   
        else:
            node = dll(key, value)
            self.hash[key] = node
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.length += 1
            if self.length > self.capacity:
                remove = self.head.next
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
                del self.hash[remove.key]
                self.length -= 1
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


#Solution2
class Node:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        
class LRUCache:   

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash = {}
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)        
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.hash:
            return -1
        
        node = self.hash[key]
        val = node.value
        
        self.removeNode(node)
        self.addToFront(node)
        
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            node = self.hash[key]
            node.value = value
            self.removeNode(node)
            self.addToFront(node)
        else:
            node = Node(key,value)
            self.hash[key] = node
            self.addToFront(node)
            if len(self.hash) > self.capacity:
                self.removeLRUEntry()
                
    def addToFront(self, node):
        node.prev = self.head
        node.next = self.head.next
        
        self.head.next.prev = node
        self.head.next = node
    
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def removeLRUEntry(self):
        del self.hash[self.tail.prev.key]
        self.removeNode(self.tail.prev)
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)