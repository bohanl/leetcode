class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        if not A: -1
        
        lo, hi = 0, len(A)-1
        while lo <= hi:
            mid = (lo + hi)/2
            if A[mid] == target:
                return mid
            if A[mid] >= A[lo]:
                if target >= A[lo] and target < A[mid]:
                    hi = mid-1
                else:
                    lo = mid+1
            else:
                if target > A[mid] and target <= A[hi]:
                    lo = mid+1
                else:
                    hi = mid-1

        return -1