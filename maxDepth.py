# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        depth_so_far = 0
        
        return self.maxDepthHelper(root, depth_so_far)
    
    def maxDepthHelper(self, root, depth_so_far):
        
        if root is None:
            return depth_so_far
        
        depth_so_far += 1
        
        return max(self.maxDepthHelper(root.left, depth_so_far), self.maxDepthHelper(root.right, depth_so_far))
        