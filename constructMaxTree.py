# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        return self.constructHelper(nums)
    
    def constructHelper(self, nums):
        # Base Condition
        
        if not nums:
            return None
        
        maxIdx = nums.index(max(nums)) # Will give me the max index
        
        node = TreeNode(nums[maxIdx])
        
        node.left = self.constructHelper(nums[: maxIdx])
        node.right = self.constructHelper(nums[maxIdx + 1:])
        
        return node