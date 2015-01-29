# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

MAX_INT = 9223372036854775807
MIN_INT = -9223372036854775808


class Solution:

    def _is_valid_bst_recursive(self, p, low, high):
        if not p: return True
        return p.val > low and \
               p.val < high and \
               self._is_valid_bst_recursive(p.left, low, p.val) and \
               self._is_valid_bst_recursive(p.right, p.val, high)

    def _is_valid_bst_stack(self, root):
        last, curr, stack = None, root, []

        while curr or len(stack) != 0:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                if last and last.val >= curr.val:
                    return False
                last, curr = curr, curr.right

        return True

    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        return self._is_valid_bst_recursive(root, MIN_INT, MAX_INT)
