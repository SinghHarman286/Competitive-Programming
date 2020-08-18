# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        return self.isSymmetricHelper(root.left, root.right)
    
    def isSymmetricHelper(self, leftNode, rightNode):
        
        if leftNode is None and rightNode is None:
            return True
        elif leftNode is None and rightNode is not None:
            return False
        elif leftNode is not None and rightNode is None:
            return False
        
        if leftNode.val != rightNode.val:
            return False
        return self.isSymmetricHelper(leftNode.left, rightNode.right) and self.isSymmetricHelper(leftNode.right, rightNode.left)
        
    
# Iterative

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        queue1 = [root.left]
        queue2 = [root.right]
        
        while queue1:
            current1 = queue1.pop(0)
            current2 = queue2.pop(0)
            
            if current1 is None and current2 is None:
                continue
            elif current1 is None and current2 is not None:
                return False
            elif current1 is not None and current2 is None:
                return False
            
            if current1.val != current2.val:
                return False
            
            queue1.append(current1.left)
            queue1.append(current1.right)
            queue2.append(current2.right)
            queue2.append(current2.left)
        
        return True