
MIN_INT = -2147483648
MAX_INT = 2147483647


class Solution:
    def _divideL(self, dividend, divisor):
        if dividend < 0:
            return -1 * self._divideL(-1 * dividend, divisor)
        if divisor < 0:
            return -1 * self._divideL(dividend, -1 * divisor)
        if divisor == 0:
            return MAX_INT
        if divisor > dividend:
            return 0

        d, nbits = divisor, 0
        while (d << 1) < dividend:
            d, nbits = d << 1, nbits+1

        return (1 << nbits) + self._divideL(dividend-d, divisor)

    # @return an integer
    def divide(self, dividend, divisor):
        res = self._divideL(dividend, divisor)
        if res > 0:
            return min(MAX_INT, res)
        if res < 0:
            return max(MIN_INT, res)
        return res
