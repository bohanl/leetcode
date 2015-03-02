# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        res = []

        if not root:
            return res

        q = collections.deque([(root, 0)])
        while len(q):
            node, level = q.popleft()
            if level == len(res):
                res.append([])

            if node.left: q.append((node.left, level+1))
            if node.right: q.append((node.right, level+1))

            res[-1].append(node.val)

        return res