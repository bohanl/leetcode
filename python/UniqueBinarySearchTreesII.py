class Solution:
    
    def generate(self, start, end):
        if start > end: return [None]
        if start == end: return [TreeNode(start)]

        res = []
        for i in xrange(start,end+1):
            for left in self.generate(start, i-1):
                for right in self.generate(i+1, end):
                    root = TreeNode(i)
                    root.left, root.right = left, right
                    res.append(root)

        return res

    # @return a list of tree node
    def generateTrees(self, n):
        return self.generate(1, n)