class Solution:

    def fms(self, A, B, k):
        m, n = len(A), len(B)

        if m > n:
            return self.fms(B, A, k)

        if m == 0:
            return B[k-1]

        if k == 1:
            return min(A[0], B[0])

        pa = min(k/2, len(A))
        pb = k - pa

        if A[pa-1] <= B[pb-1]:
            return self.fms(A[pa:], B, k-pa)
        else:
            return self.fms(A, B[pb:], k-pb)

    # @return a float
    def findMedianSortedArrays(self, A, B):
        m, n = len(A), len(B)

        if (m + n) % 2 == 0:
            return (self.fms(A, B, (m+n)/2) + self.fms(A, B, (m+n)/2+1))/2.0
        else:
            return self.fms(A, B, (m+n)/2+1)        