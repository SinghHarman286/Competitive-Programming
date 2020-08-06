# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here
		currentNode = self
		if not currentNode:
			currentNode = BST(value)
		else:
			while True:
				if value < currentNode.value:
					if currentNode.left is None:
						currentNode.left = BST(value)
						break
					currentNode = currentNode.left
				else:
					if currentNode.right is None:
						currentNode.right = BST(value)
						break
					currentNode = currentNode.right
        # Do not edit the return statement of this method.
        return self

    def contains(self, value):
        # Write your code here.
		currentNode = self
		if not currentNode:
			return False
		else:
			while True:
				if currentNode.value == value:
					return True
				elif value < currentNode.value:
					if currentNode.left is None:
						return False
					currentNode = currentNode.left
				else:
					if currentNode.right is None:
						return False
					currentNode = currentNode.right

	def getMinValue(self):
		currentNode = self
		
		while currentNode.left is not None:
			currentNode = currentNode.left
		
		return currentNode.value

    def remove(self, value, parentNode=None):
        # Write your code here.
		currentNode = self
		
		while currentNode is not None:
			
			if value < currentNode.value:
				parentNode = currentNode
				currentNode = currentNode.left
			elif value > currentNode .value:
				parentNode = currentNode
				currentNode = currentNode.right
			else:
				# we found the node
				
				# Case 1 - the node has both the childrens
				if currentNode.left is not None and currentNode.right is not None:
					# replace its value with the minimum value in the right subtree
					currentNode.value = currentNode.right.getMinValue()
					currentNode.right.remove(currentNode.value, currentNode)
				
				elif parentNode is None:
					if currentNode.left is not None:
						currentNode.value = currentNode.left.value
						currentNode.right = currentNode.left.right
						currentNode.left = currentNode.left.left
					elif currentNode.right is not None:
						currentNode.value = currentNode.right.value
						currentNode.left = currentNode.right.left
						currentNode.right = currentNode.right.right
				
				elif parentNode.left == currentNode:
					parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
				elif parentNode.right == currentNode:
					parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
				break
	
        # Do not edit the return statement of this method.
        return self
