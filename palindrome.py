def isPalindrome(string):
    # Write your code here.
    startIndex = 0
	endIndex = len(string) - 1
	
	while startIndex < endIndex:
		if string[startIndex] != string[endIndex]:
			return False
		startIndex += 1
		endIndex -= 1
	
	return True
