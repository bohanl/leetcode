class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        i, j, k = 0, len(A)-1, 0
        
        while k <= j:
            if A[k] == 0:
                A[i], A[k] = 0, A[i]
                i, k = i+1, k+1
            elif A[k] == 2:
                A[j], A[k] = 2, A[j]
                j -= 1
            else:
                k += 1