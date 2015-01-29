# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def _min_depth_recursive(self, root):
        if not root: return 0
        if not root.left: return minDepth(root.right)+1
        if not root.right: return minDepth(root.left)+1
        return min(minDepth(root.left), minDepth(root.right))+1

    def _min_depth_bfs(self, root):
        if not root:
            return 0

        depth = 1
        q, right_most = collections.deque([root]), root
        while len(q):
            node = q.popleft()
            if not node.left and not node.right:
                # found the node whose depth is the minimum
                break
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
            if node is right_most:
                depth += 1
                right_most = node.right if node.right else node.left

        return depth


    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        return self._min_depth_bfs(root)