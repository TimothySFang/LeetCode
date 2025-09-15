# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        curr = slow.next
        slow.next = None

        while curr:
            temp = curr.next
            curr.next = prev
            
            prev = curr
            curr = temp

        second = prev
        first = head

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2