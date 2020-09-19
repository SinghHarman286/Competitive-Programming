# This is an input class. Do not edit
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
	visited1 = {}
	visited2 = {}
	
	stack1 = [descendantOne]
	visited1[descendantOne.name] = descendantOne
	stack2 = [descendantTwo]
	visited2[descendantTwo.name] = descendantTwo
	
	while stack1:
		currentNode = stack1.pop()
		if currentNode == topAncestor:
			break
		if not currentNode.ancestor.name in visited1:
			visited1[currentNode.ancestor.name] = currentNode.ancestor
			stack1.append(currentNode.ancestor)
	
	while stack2:
		currentNode = stack2.pop()
		if currentNode == topAncestor:
			break
		if not currentNode.ancestor.name in visited2:
			visited2[currentNode.ancestor.name] = currentNode.ancestor
			stack2.append(currentNode.ancestor)
	
	# {B: NodeB, A: NodeA}
	# {D: True, B: True, A: True}
	
	
	for node in visited1.keys(): # [B, A]
		if node in visited2:
			return visited1[node]
	
	return None
	

    # This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
    depth1 = getDepth(topAncestor, descendantOne)
	depth2 = getDepth(topAncestor, descendantTwo)
	
	if depth1 > depth2:
		return matchHelper(descendantOne, descendantTwo, topAncestor, depth1 - depth2)
	else:
		return matchHelper(descendantTwo, descendantOne, topAncestor, depth2 - depth1)

def getDepth(ancestor, descendant):
	depth = 1
	
	while descendant != ancestor:
		depth += 1
		descendant = descendant.ancestor

	return depth

def matchHelper(one, two, ancestor, diff):
	
	while diff != 0:
		one = one.ancestor
		diff -= 1
	
	while one != two:
		one = one.ancestor
		two = two.ancestor

	return one
