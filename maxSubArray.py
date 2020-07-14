class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tempSum = 0
        maxSum = -inf
    
        for num in nums:
            tempSum += num
            if tempSum > maxSum:
                maxSum = tempSum
            if tempSum < 0:
                tempSum = 0
        return maxSum