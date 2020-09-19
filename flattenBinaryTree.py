# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # preorder transversal
        
        if root is None:
            return None
        
        array = []
        current = root
        
        array = self.flattenHelper(current, array)
        
        root = array[0]
        
        root.left = None
        root.right = None
        
        for i in range(1, len(array)):
            root.right = TreeNode(array[i].val)
            root = root.right
        
    
    def flattenHelper(self, root, array):
        if root is not None:
            array.append(root)
            self.flattenHelper(root.left, array)
            self.flattenHelper(root.right, array)
        
        return array
            
            