# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        left, right = ListNode(0), ListNode(0)
        pl, pr = left, right

        while head:
            if head.val < x:
                pl, pl.next = pl.next, head
            else:
                pr, pr.next = pr.next, head
            head = head.next

        pl.next, pr.next = right.next, None

        return left.next