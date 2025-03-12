# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head1, head2 = list1, list2

        dummyHead = ListNode()
        headPrev = dummyHead

        while head1 and head2:
            if head1.val < head2.val:
                dummyHead.next = head1
                head1 = head1.next
            else:
                dummyHead.next = head2
                head2 = head2.next
            dummyHead = dummyHead.next
        
        if head1:
            dummyHead.next = head1
        elif head2:
            dummyHead.next = head2
        
        return headPrev.next

        #time O(n), space O(1)
