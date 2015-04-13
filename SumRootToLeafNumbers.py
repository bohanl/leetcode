# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def backtrack(self, node, a, arr):
        a = a*10 + node.val
        if not node.left and not node.right:
            arr.append(a)
            return
        if node.left:
            self.backtrack(node.left, a, arr)
        if node.right:
            self.backtrack(node.right, a, arr)

    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        a, arr = 0, []
        if root:
            self.backtrack(root, a, arr)
        return sum(arr)
