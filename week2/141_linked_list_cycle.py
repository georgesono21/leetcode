# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        """
        floyds tortise and hare. if there's a cycle in the linkedlist, 
        the fast pointer will eventually catch up to the slow pointer 
        bc it's going in circles
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True 
        
        return False

        #time O(1) space O(1)
        
