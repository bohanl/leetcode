class Solution:
    def _is_symmetric_recursive(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        
        return left.val == right.val and \
               self._is_symmetric_recursive(left.left, right.right) and \
               self._is_symmetric_recursive(left.right, right.left)

    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if not root: return True
        return self._is_symmetric_recursive(root.left, root.right)