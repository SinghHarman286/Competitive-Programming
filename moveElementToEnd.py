# Solution 1

# Time Complexity: O(n) Space Complexity: O(1)
def moveElementToEnd(array, toMove):
    # Write your code here.
    i = 0
    j = 0
    print("can you see me")
    if toMove not in array:
        return array
    
    while j < len(array):
        print(i, j)
        if array[j] == toMove:
            j += 1
            continue
        array[i] = array[j]
        i += 1
        j += 1
    
    while i < len(array):
        array[i] = toMove
        i += 1
    
    return array

# Solution 2
def moveElementToEnd2(array, toMove):
    i = 0
    j = len(array) - 1

    while i < j:
        while j < i and array[j] == toMove:
            j -= 1
        
        if array[i] == toMove:
            array[i], array[j] = array[j], array[i]
        
        i += 1
    
    return array

# Solution 3

def moveElementToEnd3(array, toMove):
	# O(n^2)
    for num in array:
		if num == toMove:
			array.remove(num)
			array.append(num)
			
	return array

# Solution 4

def moveElementToEnd(array, toMove):
	# O(n)
	if toMove not in array:
		return array
    num = array.count(toMove)
	array = list(set(array))
	array.remove(toMove)
	array.extend([toMove for i in range(num)])
	return array