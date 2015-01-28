# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        # n will always be valid
        dummy = ListNode(0)
        dummy.next = head

        p1, p2 = dummy, dummy
        for _ in xrange(n):
            p2 = p2.next

        while p2.next:
            p1 = p1.next
            p2 = p2.next

        p1.next = p1.next.next

        return dummy.next