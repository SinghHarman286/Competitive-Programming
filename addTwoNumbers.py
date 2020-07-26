class Solution:
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        zero1 = 1
        zero2 = 1
        num1 = 0
        num2 = 0
        
        while l1:
            num1 += l1.val * zero1
            zero1 *= 10
            l1 = l1.next
        
        while l2:
            num2 += l2.val * zero2
            zero2 *= 10
            l2 = l2.next
        
        num = num1 + num2
        
        l = ListNode()
        
        self.giveList(l, num)
        
        return l
    
    def giveList(self, l, num):

        firstNum = num % 10
        num //= 10
        l.val = firstNum
        if num == 0:
            return
        else:
            l.next = ListNode()
            self.giveList(l.next, num)


# Other Solution SC: O(1) | TC: O(n)