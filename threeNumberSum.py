def threeNumberSum(array, targetSum):
    # Write your code here.
	array.sort()
	triplets = []
	
	for i in range(len(array) - 2):
		left = i + 1
		right = len(array) - 1
		
		while left < right:
			currentSum = array[i] + array[left] + array[right]
			if currentSum == targetSum:
				triplets.append([array[i], array[left], array[right]])
				left += 1
				right -= 1
			elif currentSum < targetSum:
				left += 1
			else:
				right -= 1
				
	return triplets
