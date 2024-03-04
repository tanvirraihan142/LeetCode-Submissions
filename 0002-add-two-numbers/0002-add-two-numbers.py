# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        temp = dummy
        
        while (l1 != None or l2 != None or carry):
            Sum = 0
            if (l1 != None):
                Sum += l1.val
                l1 = l1.next
                
            if (l2 != None):
                Sum += l2.val
                l2 = l2.next
                
            Sum += carry
            carry = Sum//10
            newNode = ListNode(Sum%10)
            temp.next = newNode
            temp = temp.next
        
        return dummy.next