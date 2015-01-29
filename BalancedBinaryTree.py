# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def maxDepth(self, root):
        if not root:
            return 0
        return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))

    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if not root:
            return True
        return abs(self.maxDepth(root.left)-self.maxDepth(root.right))<=1 and \
               self.isBalanced(root.left) and \
               self.isBalanced(root.right)