# Time: O(n) | Space: O(n)
def maxSubsetSumNoAdjacent(array):
    # Write your code here.
    if len(array) == 0:
		return 0
	elif len(array) == 1:
		return array[0]
	
	maxSumArr = array[:]
	# array = [75, 105, 120, 75, 90, 135]
	maxSumArr[0] = array[0] 
	maxSumArr[1] = max(array[0], array[1])
	# maxSumArr = [75, 105]
	
	for i in range(2, len(array)):
		maxSumArr[i] = max(maxSumArr[i-1], maxSumArr[i-2] + array[i])
	
	return maxSumArr[-1]

# Time: O(n) | Space: O(1)
def maxSubsetSumNoAdjacent(array):
    # Write your code here.
    if len(array) == 0:
		return 0
	elif len(array) == 1:
		return array[0]
	
	# maxSumArr = [first, second]
	# maxSumArr[2] = max(second, first + arr[2])
	
	# array = [10, 5] => 10 
	# maxSumArr = [10, ]
	
	first = array[0]
	second = max(array[0], array[1])
	
	for i in range(2, len(array)):
		current = max(second, first + array[i])
		first = second
		second = current
	
	return second