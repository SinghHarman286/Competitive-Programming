def hasSingleCycle(array):
    # Write your code here.
    
	visited = {}
	
	# {0: True, 2: True, 3: True, 6: True, 1: True,  4: True}
	index = 0
	startIndex = 0
	
	while True:
		if index in visited:
			if len(visited.keys()) == len(array) and index == startIndex:
				return True
			else:
				return False
		
		visited[index] = True
		
		# if len(visited.keys()) == len(array):
		# 	return True
		
		index += array[index]
		
		index %= len(array)
	
	return False