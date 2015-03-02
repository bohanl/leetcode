class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        n = len(A)

        left, right = [0]*n, [0]*n
        for i, j in zip(xrange(n), xrange(n-1,-1,-1)):
            left[i] = max(left[i-1], A[i]) if i > 0 else A[i]
            right[j] = max(right[j+1], A[j]) if j < n-1 else A[j]

        water = 0
        for i in xrange(1,n-1):
            low_bar = min(left[i-1], right[i+1])
            water += max(0, low_bar-A[i])*1

        return water