class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        T = [[0]*n for i in xrange(m)]
        
        for j in xrange(n): T[0][j] = 1
        for i in xrange(m): T[i][0] = 1
        
        for i in xrange(1,m):
            for j in xrange(1,n):
                T[i][j] = T[i-1][j]+T[i][j-1]
        
        return T[-1][-1]