class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n == 0:
            return 1

        y = pow(x, abs(n)/2)
        res = y * y

        if abs(n) & 1:
            res *= x

        if n < 0:
            res = 1/res

        return res