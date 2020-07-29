# Stacks - LIFO

# 4 basic Operations
    # push
    # pop
    # isEmpty
    # Top

# Using Arrays

class Stack1:
    def __init__(self):
        self.item = []
    
    def push(self, val):
        self.item.append(val)
    
    def pop(self):
        return self.item.pop()
    
    def isEmpty(self):
        return len(self.item) == 0
    
    def top(self):
        if self.isEmpty():
            return None
        return self.item[len(self.item) - 1]

    def print(self):
        print(self.item)

myStack = Stack1()

myStack.print() # []

myStack.push(3)
myStack.push(2)
myStack.push(5)

myStack.print() # [3, 2, 5]

myStack.pop() # [3, 2]
myStack.print()
myStack.pop() # [3]
print(myStack.top()) # 3
myStack.print()
myStack.pop()
myStack.print()
print(myStack.isEmpty())

# # We can use unshift and shift also but the timeComplexity will be O(n) in that case!

# Using Linked List
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Stack2:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
    
    def push(self, val):
        newNode = Node(val)
        if not self.first:
            self.first = newNode
            self.last = newNode
        else:
            currHead = self.first
            self.first = newNode
            self.first.next = currHead
        
        self.size += 1
        return self.size
    
    def pop(self):
        if not self.first:
            return None
        
        currHead = self.first

        if self.first == self.last:
            self.last = None
        
        self.first = self.first.next

        self.size -= 1

        return currHead.data
    
    def isEmpty(self):
        return not self.first
    
    def top(self):
        if not self.isEmpty():
            return self.first.data
        
        return None
    
    def printl(self):
        arr = []

        current = self.first

        while current:
            arr.append(current.data)
            current = current.next
        
        print(arr)

myStack = Stack2()

myStack.printl()

myStack.push(3)
myStack.push(4)
myStack.push(5)
myStack.printl()
myStack.pop()
myStack.printl()
myStack.pop()
myStack.printl()
print(myStack.top())
print(myStack.isEmpty())