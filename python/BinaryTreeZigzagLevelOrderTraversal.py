class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        res = []

        if not root: return res

        curr_level, q = -1, collections.deque([(root, 0)])
        reversed = True

        while q:
            node, level = q.popleft()

            if node.left: q.append((node.left, level+1))
            if node.right: q.append((node.right, level+1))

            if level > curr_level:
                res.append([])
                curr_level, reversed = level, not reversed

            if reversed:
                res[-1].insert(0, node.val)
            else:
                res[-1].append(node.val)

        return res