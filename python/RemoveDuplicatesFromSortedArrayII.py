class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) < 3:
            return len(A)

        i = 1
        for j in xrange(2, len(A)):
            if A[i-1] != A[j]:
                i += 1
                A[i] = A[j]

        return i + 1