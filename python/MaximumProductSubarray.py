class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        n = len(A)

        res, max_, min_ = A[0], A[0], A[0]
        for i in xrange(1, n):
            tmp_max = max_
            max_ = max(max_*A[i], A[i], min_*A[i])
            min_ = min(tmp_max*A[i], A[i], min_*A[i])
            res = max(max_, res)

        return res