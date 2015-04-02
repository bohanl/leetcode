class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        s1, s2 = 1, 1
        for i in xrange(2,n+1):
            s1, s2 = s2, s1+s2

        return s2