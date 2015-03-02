class Solution:
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        T = [[0]*n for i in xrange(m)]
        
        for j in xrange(n):
            if obstacleGrid[0][j]:
                break
            T[0][j] = 1

        for i in xrange(m):
            if obstacleGrid[i][0]:
                break
            T[i][0] = 1
        
        for i in xrange(1,m):
            for j in xrange(1,n):
                if obstacleGrid[i][j]:
                    T[i][j] = 0
                else:
                    T[i][j] = T[i-1][j]+T[i][j-1]
        
        return T[-1][-1]