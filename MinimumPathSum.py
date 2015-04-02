class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])

        T = [[0] * n for i in xrange(m)]
        T[0][0] = grid[0][0]

        for j in xrange(1,n):
            T[0][j] = T[0][j-1]+grid[0][j]

        for i in xrange(1,m):
            T[i][0] = T[i-1][0]+grid[i][0]

        for i in xrange(1,m):
            for j in xrange(1,n):
                T[i][j] = min(T[i-1][j], T[i][j-1]) + grid[i][j]

        return T[-1][-1]