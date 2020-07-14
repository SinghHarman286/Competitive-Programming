# Time: O(nlogn) | SpaceComplexity: O(1)

def twoNumberSum(array, targetSum):
    array.sort()
	left = 0
	right = len(array) - 1

	while(left < right):
		sum = array[left] + array[right]
		result = [array[left], array[right]]

		if sum == targetSum:
			return result
		elif sum < targetSum:
			left += 1
		else:
			right -= 1

	return []
