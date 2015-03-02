class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        # assuming x >= 0
        if x == 0: return 0

        k = 1
        while k*k < x:
            k <<= 1
        
        lo, hi = k/2, k
        while lo <= hi:
            mid = (lo+hi)/2
            prd = mid*mid
            if prd == x:
                return mid
            elif prd > x:
                hi = mid-1
            else:
                lo = mid+1
        
        return lo-1