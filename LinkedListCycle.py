# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def _has_cycle(self, head):
        seen = set([])

        curr = head
        while curr:
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.next

        return False

    def _has_cycle_two_pointers(self, head):
        if not head:
            return False

        p1, p2 = head, head
        while p1 and p2 and p2.next:
            p1, p2 = p1.next, p2.next.next
            if p1 is p2:
                return True

        return False

    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        return self._has_cycle_two_pointers(head)       