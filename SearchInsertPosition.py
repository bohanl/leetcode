class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        if not A: return -1
        lo, hi = 0, len(A)-1

        while lo<=hi:
            mid = (lo+hi)/2
            if A[mid] == target:
                return mid
            elif A[mid] > target:
                hi = mid-1
            else:
                lo = mid+1

        return lo
