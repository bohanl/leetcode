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
                pl.next = head
                pl = pl.next
            else:
                pr.next = head
                pr = pr.next
            head = head.next

        pl.next = right.next
        pr.next = None

        return left.next