class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
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

        while current.next is not None:
            newTail = current
            current = current.next
        
        self.tail = newTail
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
        
        return current
    
    def shift(self):
        if not self.head:
            return None

        currentHead = self.head
        self.head = currentHead.next
        self.length -= 1

        if self.length == 0:
            self.tail = None
        
        return currentHead
    
    def unshift(self, value):
        newNode = Node(value)
        
        if not self.head:
            self.head = newNode
            self.tail = self.head
        
        newNode.next = self.head
        self.head = newNode
        self.length += 1

        return self
    
    def get(self, index):
        if index < 0 or index > self.length:
            return None
        
        current = self.head
        counter = 0

        while counter != index:
            current = current.next
            counter += 1
        
        return current
    
    def set(self, index, value):
        node = self.get(index)

        if node:
            node.data = value
            return True
        
        return False
    
    def insert(self, index, value):
        newNode = Node(value)

        if index < 0 or index > self.length:
            return False
        elif index == 0:
            self.unshift(value)
            return True
        elif index == self.length:
            self.push(value)
            return True
        else:
            prevNode = self.get(index - 1)
            tempNode = prevNode.next
            prevNode.next = newNode
            newNode.next = tempNode
            self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.shift()
        elif index == self.length - 1:
            return self.pop()
        else:
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

