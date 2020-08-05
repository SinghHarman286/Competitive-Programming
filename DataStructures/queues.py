# Queues - FIFO

# 4 Basic Operations
# Enqueue - adds
# Dequeue - removes
# Front - Front Item
# isEmpty

# Using Arrays
class Queues1:
    def __init__(self):
        self.item = []
    
    def enqueue(self, val):
        self.item.append(val) # can use unshift here
    
    def dequeue(self):
        return self.item.pop(0) # use pop if used unshift
    
    def isEmpty(self):
        return len(self.item) == 0

    def front(self):
        if not self.isEmpty():
            return self.item[0]
        return None
    
    def print(self):
        print(self.item)

# Test Cases

queue1 = Queues1()

queue1.print()
queue1.enqueue(2)
queue1.print()
queue1.enqueue(4)
queue1.print()
queue1.dequeue()
queue1.print()
print(queue1.front())
print(queue1.isEmpty())
queue1.enqueue(5)
queue1.enqueue(10)
queue1.dequeue()
queue1.print()
queue1.dequeue()
queue1.dequeue()
print(queue1.isEmpty())

# Using LinkedList


print("\n\nqueue2 is starting \n=====\n")

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Queues2:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
    
    def enqueue(self, val):
        newNode = Node(val)
        if not self.first:
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        
        self.length += 1
        return self.length
    
    def dequeue(self):
        if not self.first:
            return None

        if self.first == self.last:
            self.last = None
        
        temp = self.first

        self.first = self.first.next
        self.length -= 1
        
        return temp.data
    
    def isEmpty(self):
        return not self.first
    
    def front(self):
        if not self.first:
            return None
        return self.first.data
    
    def print(self):
        arr = []
        current = self.first

        while current:
            arr.append(current.data)
            current = current.next
        
        print(arr)

# Test Cases
queue2 = Queues2()

queue2.print()
queue2.enqueue(3)
queue2.enqueue(4)
queue2.enqueue(5)
queue2.print()
queue2.dequeue()
queue2.print()
queue2.dequeue()
queue2.print()
print(queue2.front())
print(queue2.isEmpty())



