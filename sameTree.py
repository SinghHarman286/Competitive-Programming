# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive Solution
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
             return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Iterative
# Definition for a binary tree node.

class Solution:
    def check1(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        return True
    
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # Iterative Solution
        queue = [(p, q)]
        
        while queue:
            p, q = queue.pop(0)
            
            if not self.check1(p, q):
                return False
            
            if p:
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))
        
        return True

