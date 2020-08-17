# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    # Write your code here.
    return validateBstHelper(tree, float('-inf'), float('inf'))

def validateBstHelper(tree, minValue, maxValue):
	if tree is None:
		return True
	# neg (tree.value must be >= minValue and tree.value must be < maxValue)
	if tree.value < minValue or tree.value >= maxValue:
		return False
	
	leftIsValid = validateBstHelper(tree.left, minValue, tree.value)
	rightIsValid = validateBstHelper(tree.right, tree.value, maxValue)
	return leftIsValid and rightIsValid

#====================LEETCODE VERSION============================

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        current = root
        minValue = float('-inf')
        
        while current or stack:
            
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                if current.val <= minValue:
                    return False
                minValue = current.val
                current = current.right
        
        return True
