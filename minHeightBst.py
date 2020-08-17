# 1 

def minHeightBst(array):
	return constructBST(array, None, 0, len(array) - 1)

def constructBST(array, bst, startIdx, endIdx):
	if endIdx < startIdx:
		return
	
	midIdx = (startIdx + endIdx) // 2
	valueToAdd = array[midIdx]
	
	if not bst:
		bst = BST(valueToAdd)
	else:
		bst.insert(valueToAdd)
	
	constructBST(array, bst, startIdx, midIdx - 1)
	constructBST(array, bst, midIdx + 1, endIdx)
	
	return bst


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

# 2

def minHeightBst(array):
    return constructBST(array, None, 0, len(array) - 1)

def constructBST(array, bst, startIdx, endIdx):
	if endIdx < startIdx:
		return
	
	midIdx = (startIdx + endIdx) // 2
	valueToadd = array[midIdx]
	
	if not bst:
		bst = BST(valueToadd)
	else:
		if valueToadd < bst.value:
			bst.left = BST(valueToadd)
			bst = bst.left
		else:
			bst.right = BST(valueToadd)
			bst = bst.right
		
	constructBST(array, bst, startIdx, midIdx - 1)
	constructBST(array, bst, midIdx + 1, endIdx)
	
	return bst

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


# 3
def minHeightBst(array):
    return constructBST(array, 0, len(array) - 1)

def constructBST(array, startIdx, endIdx):
	if endIdx < startIdx:
		return
	
	midIdx = (startIdx + endIdx) // 2
	valueToadd = array[midIdx]
	
	bst = BST(valueToadd)
	
	bst.left = constructBST(array, startIdx, midIdx - 1)
	bst.right = constructBST(array, midIdx + 1, endIdx)
	
	return bst

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
