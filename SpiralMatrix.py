class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        res = []
        
        if not matrix:
            return res
        
        rmin, cmin = 0, 0
        rmax, cmax = len(matrix)-1, len(matrix[0])-1

        while True:
            if cmin > cmax:
                break
            res.extend([matrix[rmin][j] for j in xrange(cmin, cmax+1)])
            rmin += 1

            if rmin > rmax:
                break
            res.extend([matrix[i][cmax] for i in xrange(rmin, rmax+1)])
            cmax -= 1

            if cmax < cmin:
                break
            res.extend([matrix[rmax][j] for j in xrange(cmax, cmin-1, -1)])
            rmax -= 1

            if rmax < rmin:
                break
            res.extend([matrix[i][cmin] for i in xrange(rmax, rmin-1, -1)])
            cmin += 1

        return res