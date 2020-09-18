# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        
        if root is None:
            return 0
        
        width = 1
        
        q = deque([(root, 0)])
        
        while q:
            _, leftIdx = q[0]
            _, rightIdx = q[-1]
            
            width = max(width, rightIdx - leftIdx + 1)
            
            next_level = deque()
            
            while q:
                
                node, index = q.popleft()
                
                if node.left: next_level.append((node.left, 2*index))
                if node.right: next_level.append((node.right, 2*index + 1))
            
            q = next_level
        
        return width