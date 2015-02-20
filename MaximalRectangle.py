class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        height = [[0]*n for i in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == '1':
                    height[i][j] = height[i-1][j] + 1 if i>0 else 1

        max_area = 0
        for k in xrange(m):
            for i in xrange(n-1,-1,-1):
                min_bar = height[k][i]
                if i == n-1 or height[k][i] > height[k][i+1]:
                    for j in xrange(i, -1, -1):
                        min_bar = min(height[k][j], min_bar)
                        max_area = max(max_area, min_bar*(i-j+1))

        return max_area
