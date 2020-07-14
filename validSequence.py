# Time: O(n) | SpaceComplexity: O(1)

def isValidSubsequence(array, sequence):
    # Write your code here.
    if len(sequence) > len(array):
		return False
	i = 0
	for num in array:
		if num == sequence[i]:
			i += 1
		if i == len(sequence):
			return True
	return False