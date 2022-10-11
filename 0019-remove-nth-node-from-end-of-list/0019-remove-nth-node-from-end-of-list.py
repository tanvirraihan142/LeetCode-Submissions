# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        curr1 = dummy
        curr2 = dummy
        
        for i in range(n+1):
            curr1 = curr1.next
        
        while curr1:
            curr1 = curr1.next
            curr2 = curr2.next
        
        curr2.next = curr2.next.next
        return dummy.next