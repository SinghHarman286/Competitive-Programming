class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
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
            newNode.prev = self.tail
            newNode.next = None
            self.tail = newNode
        self.length += 1
        return self

    def pop(self):
        if not self.head:
            return None
        removedNode = self.tail
        newTail = removedNode.prev
        newTail.next = None
        self.tail = newTail
        removedNode.prev = None

        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        
        return removedNode

    def unshift(self, value):
        newHead = Node(value)
        if not self.head:
            self.head = newHead
            self.tail = self.head
        else:
            newHead.next = self.head
            self.head.prev = newHead
            self.head = newHead
        self.length += 1
        return self
    
    def shift(self):
        if not self.head:
            return None
        
        removedNode = self.head
        self.head = removedNode.next
        self.head.prev = None
        removedNode.next = None

        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
        
        return removedNode
    
    def get(self, index):
        if index < 0 or index > self.length:
            return None
        
        if index <= self.length / 2:
            current = self.head
            counter = 0

            while counter != index:
                counter += 1
                current = current.next
            
            return current
        else:
            current = self.tail
            counter = self.length - 1

            while counter != index:
                counter -= 1
                current = current.prev
            
            return current
        
    def set(self, index, value):
        foundNode = self.get(index)

        if foundNode:
            foundNode.data = value
            return True
        
        return False
    
    def insert(self, index, value):
        if index < 0  or index > self.length:
            return False
        if index == 0:
            self.unshift(value)
            return True
        if index == self.length:
            self.push(value)
            return True
        
        prevNode = self.get(index - 1)
        nextNode = self.get(index)
        newNode = Node(value)
        prevNode.next = newNode
        newNode.prev = prevNode
        newNode.next = nextNode
        nextNodeprev = newNode

        self.length += 1

        return True
    
    def remove(self, index):
        if index < 0  or index > self.length:
            return None
        if index == 0:
            self.shift()
            return self
        if index == self.length:
            self.pop()
            return self
        
        prevNode = self.get(index - 1)
        removedNode = prevNode.next
        nextNode = removedNode.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        removedNode.next = None
        removedNode.prev = None
        
        self.length -= 1

        return self

    def reverse(self):
        node = self.head
        self.head = self.tail
        self.tail = node

        next = None
        prev = None
        while node:
            next = node.next
            node.next = prev
            node.prev = next
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

dll = DoublyLinkedList()

# Test Cases

dll.push(2)
dll.push(3)
dll.push(124)
dll.push(12412)
dll.pop()
dll.shift()
dll.unshift(999)
dll.set(0, 1000)
dll.insert(0, 12412)
dll.remove(1)
dll.print() # [12412, 3, 124]
dll.reverse() # [124, 3, 12412]
dll.print()

print(dll.length)