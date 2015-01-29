# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def _is_valid_bst_recursive(self, root):
        rval = root.val

        left_valid, right_valid = True, True        
        if root.left:
            left_valid = root.left.val < rval and isValidBST(root.left)
        if left_valid and root.right:
            right_valid = root.right.val > rval and isValidBST(root.right)

        return left_valid and right_valid

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
        if not root:
            return True
        
        return self._is_valid_bst_stack(root)
