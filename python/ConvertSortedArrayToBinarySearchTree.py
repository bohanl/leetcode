# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def _sorted_array_to_bst(self, num, p, q):
        if p > q:
            return None

        r = (p+q) / 2

        node = TreeNode(num[r])
        node.left = self._sorted_array_to_bst(num, p, r-1)
        node.right = self._sorted_array_to_bst(num, r+1, q)

        return node

    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        return self._sorted_array_to_bst(num, 0, len(num)-1)
