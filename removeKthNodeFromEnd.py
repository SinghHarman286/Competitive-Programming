# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # Write your code here.
	if k == 0:
		return
		
    nodeFromBeg = length(head) - k
	
	# Checking if its a head
	if nodeFromBeg == 0:
		currHead = head
		nextHead = currHead.next
		currHead.value = nextHead.value
		currHead.next = nextHead.next
		return
	
	prev = None
	index = 0
	
	while index != nodeFromBeg:
		prev = head
		head = head.next
		index += 1
	
	prev.next = head.next
	return

def length(node):
	length = 0
	while node:
		length += 1
		node = node.next
	
	return length