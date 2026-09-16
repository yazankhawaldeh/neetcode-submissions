# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow = head
        fast = head
        while (slow):
            slow = slow.next
            if fast == None or fast.next == None or fast.next.next == None:
                return False
            else:
                fast = fast.next.next
            if slow == fast:
                return True
                
        