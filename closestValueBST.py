def findClosestValueInBst(tree, target):
    # Write your code here.
    currentNode = tree
	closestTillNow = tree
	minNode = tree.value
	
	while currentNode is not None:
		if abs(closestTillNow.value - target) > abs(currentNode.value - target):
			closestTillNow = currentNode
		if target > currentNode.value:
			currentNode = currentNode.right
		elif target < currentNode.value:
			currentNode = currentNode.left
		else:
			return currentNode.value
	
	return closestTillNow.value
	


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
