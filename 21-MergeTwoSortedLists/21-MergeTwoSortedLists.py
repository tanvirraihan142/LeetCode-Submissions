# Last updated: 5/17/2025, 6:28:30 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2

        
        dummy_head = ListNode(0, None)
        curr = dummy_head

        while head1 is not None and head2 is not None:
            if head1.val <= head2.val:
                curr.next = head1
                head1 = head1.next 
            else:
                curr.next = head2
                head2 = head2.next 
                
            curr = curr.next

        if head1 is not None:
            curr.next = head1
        elif head2 is not None:
            curr.next = head2
        

        return dummy_head.next
            

        