class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        T = [0] * len(A)

        max_, T[0] = A[0], A[0]
        for i in xrange(1, len(A)):
            T[i] = max(T[i-1] + A[i], A[i])
            if T[i] > max_:
                max_ = T[i]

        return max_