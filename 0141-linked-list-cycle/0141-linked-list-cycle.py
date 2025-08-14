# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return False
        fast, slow = head.next.next, head.next

        while fast and fast.next:
            if fast == slow:
                return True
            else:
                fast = fast.next.next
                slow = slow.next

        return False