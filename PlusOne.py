class Solution:
    def plusOne(self, nums: List[int]) -> List[int]:
        lastPos = len(nums) - 1
        while (True):
            nums[lastPos] += 1
            if nums[lastPos] > 9:
                carry = 1
                remainder = nums[lastPos] % 10
                nums[lastPos] = remainder
                lastPos -= 1
                if lastPos < 0:
                    nums.insert(0, carry)
                    break
                else:
                    continue
            else:
                break
        return nums