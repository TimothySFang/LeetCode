# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        summation = ListNode()
        head = summation
        carry_over = False
        while (l1 or l2):
            if l1 == None:
                l1 = ListNode(val= 0)
            if l2 == None:
                l2 = ListNode(val= 0)
            new_digit = 0
            if carry_over:
                new_digit = 1 + l1.val + l2.val
            else:
                new_digit = l1.val + l2.val

            if new_digit > 9:
                carry_over = True
                summation.next = ListNode(val = new_digit - 10)
            else: 
                carry_over = False
                summation.next = ListNode(val = new_digit)
            summation = summation.next
            l1 = l1.next
            l2 = l2.next
        if carry_over:
            summation.next = ListNode(val = 1)
        return head.next