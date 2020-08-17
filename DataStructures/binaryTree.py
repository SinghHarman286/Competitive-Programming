class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        newNode = Node(value)
        if not self.root:
            self.root = newNode
        
        current = self.root

        while True:
            if current.value == value:
                return None
            elif value < current.value:
                if current.left is None:
                    current.left = newNode
                    return self
                current = current.left
            elif value > current.value:
                if current.right is None:
                    current.right = newNode
                    return self
                current = current.right
    
    def find(self, value):
        if not self.root:
            return False
        
        current = self.root

        while True:
            if current.value == value:
                return True
            elif value < current.value:
                if current.left is None:
                    return False
                current = current.left
            elif value > current.value:
                if current.right is None:
                    return False
                current = current.right

    def BFS(self):
        node = self.root
        queue = []
        data = []
        queue.append(node)
        while queue:
            node = queue.pop(0)
            data.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return data
    
    def DFSPreOrder(self):
        data = []
        def transverse(node):
            data.append(node.value)
            if node.left:
                transverse(node.left)
            if node.right:
                transverse(node.right)
        transverse(self.root)
        return data
    def DFSInOrder(self):
        data = []
        def transverse(node):
            if node.left:
                transverse(node.left)
            data.append(node.value)
            if node.right:
                transverse(node.right)
        transverse(self.root)
        return data
    
    def DFSInOrder2(self):
        stack = []
        data = []
        current = self.root

        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                current = current.right
        return data


    def DFSPostOrder(self):
        data = []
        def transverse(node):
            if node.left:
                transverse(node.left)
            if node.right:
                transverse(node.right)
            data.append(node.value)
        transverse(self.root)
        return data

tree = BST()
tree.insert(10)
tree.insert(6)
tree.insert(15)
tree.insert(3)
tree.insert(8)
tree.insert(20)

#       10
#     /    \
#   6        15
#  / \         \
# 3   8         20

print(tree.BFS()) # [10, 6, 15, 3, 8, 20]
print(tree.DFSPreOrder()) # [10, 6, 3, 8, 15, 20]
print(tree.DFSInOrder()) # [3, 6, 8, 10, 15, 20]
print(tree.DFSPostOrder()) # [3, 8, 6, 20, 15, 10]
print(tree.DFSInOrder2()) # [3, 6, 8, 10, 15, 20]