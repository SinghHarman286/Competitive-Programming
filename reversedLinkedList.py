def reverseLinkedList(head):
    # Write your code here.
    node = head
	
	next = None
	prev = None
	
	while node:
		next = node.next # next is 2
		node.next = prev # 1-> 0 -> None
		prev = node # prev is 1
		node = next # node is 2
	
	head = prev
	
	return head
		
		