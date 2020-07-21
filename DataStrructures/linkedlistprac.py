# Node
class Node:
    def __init__(self, value):
        # 2 properties
        self.data = value
        self.next = None

# Linked List
class LinkedList:
    def __init__(self):
        # 3 properties
        self.head = None # -> Node
        self.tail = None # -> Node
        self.length = 0 # -> Int
    
    def push(self, value):
        newNode = Node(value)

        if not self.head:
            self.head = newNode
            self.tail = self.head
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1

        return self
    
    def pop(self):
        if not self.head:
            return None
        
        current = self.head
        newTail = current

        # 1->2->None
        while current.next:
            newTail = current
            current = current.next

        self.tail = newTail
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
        
        return current
    
    def unshift(self, value):
        newNode = Node(value)

        if not self.head:
            self.head = newNode
            self.tail = self.head
        else:
            currentHead = self.head
            self.head = newNode
            self.head.next = currentHead
        
        self.length += 1
        return self
    
    def shift(self):
        if not self.head:
            return None
        
        currentHead = self.head
        self.head = currentHead.next
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
        
        return currentHead
    
    def get(self, index):
        if index < 0 or index > self.length:
            return None
        current = self.head
        counter = 0

        while counter != index:
            current = current.next
            counter += 1

        return current
    
    def set(self, value, index):
        if index < 0 or index > self.length:
            return False
        node = self.get(index)

        if node:
            node.data = value
            return True
        
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            self.unshift(value)
            return True
        if index == self.length:
            self.push(value)
            return True
        
        newNode = Node(value)
        prev = self.get(index - 1)
        tempNode = prev.next
        prev.next = newNode
        newNode.next = tempNode

        self.length += 1

        return True

    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            self.shift()
            return self
        if index == self.length:
            self.pop()
            return self
        prevNode = self.get(index - 1)
        removedNode = prevNode.next
        prevNode.next = removedNode.next
        self.length -= 1

        return self
    
    def reverse(self):
        node = self.head
        self.head = self.tail
        self.tail = node

        prev = None
        next = None

        while node:
            next = node.next
            node.next = prev
            prev = node
            node = next
        
        return self

        
    def print(self):
        arr = []
        current = self.head

        while current:
            arr.append(current.data)
            current = current.next
        
        print(arr)

linkedList = LinkedList()
linkedList.push(1)
linkedList.push(2)
linkedList.push(4)
linkedList.push(5)
linkedList.push(6)
linkedList.push(7)
linkedList.print()

linkedList.reverse()
linkedList.print()

