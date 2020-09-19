def riverSizes(matrix):
    # Write your code here.
	sizes = []
	visited = [[False for value in row] for row in matrix]
	
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if visited[i][j]:
				continue
			dfs(matrix, visited, sizes, i, j)
	return sizes

def dfs(matrix, visited, sizes, i, j):
	currentSize = 0	
	nodeToExplore = [[i, j]]
	
	while len(nodeToExplore):
		currentNode = nodeToExplore.pop()
		row = currentNode[0]
		col = currentNode[1]	
		if visited[row][col]:
			continue
		visited[row][col] = True
		if matrix[row][col] == 0:
			continue
		currentSize += 1
		newArr = getNeighbours(matrix, visited, i, j)
		for item in newArr:
			nodeToExplore.append(item)	
	if currentSize > 0:
		sizes.append(currentSize)

def getNeighbours(matrix, visited, i, j):
	array = []
	if i > 0 and not visited[i - 1][j]:
		array.append([i-1, j])
	if i < len(matrix) - 1 and not visited[i+1][j]:
		array.append([i+1, j])
	if j > 0 and not visited[i][j-1]:
		array.append([i, j-1])
	if j < len(matrix) - 1 and not visited[i][j + 1]:
		array.append([i, j + 1])
	return array