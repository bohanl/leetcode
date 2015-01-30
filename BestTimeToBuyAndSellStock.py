class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if not prices:
            return 0

        minval, maxp = prices[0], 0
        for i in xrange(1, len(prices)):
            minval = min(minval, prices[i])
            maxp = max(maxp, prices[i]-minval)

        return maxp
