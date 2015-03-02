# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, a non-negative integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if k == 0: return head

        dummy = ListNode(0)
        dummy.next = head

        p1, p2 = dummy, dummy
        while k > 0:
            p2, k = p2.next, k-1
            if not p2: p2 = head

        while p2 and p2.next:
            p1, p2 = p1.next, p2.next

        rhead, p1.next = p1.next, None
        if p2 and p1 is not dummy: p2.next = head

        return rhead