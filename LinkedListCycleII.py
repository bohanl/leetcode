# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def _detect_cycle(self, head):
        seen = set([])

        curr = head
        while curr:
            if curr in seen:
                return curr
            seen.add(curr)
            curr = curr.next

        return None

    def _detect_cycle_two_pointers(self, head):
        found = False
        
        p1, p2 = head, head
        
        while not found and p1 and p2 and p2.next:
            p1, p2 = p1.next, p2.next.next
            if p1 is p2: found = True

        if not found:
            return None

        p1 = head
        while p1 is not p2: p1, p2 = p1.next, p2.next
        
        return p1

    # @param head, a ListNode
    # @return a boolean
    def detectCycle(self, head):
        return self._detect_cycle_two_pointers(head)