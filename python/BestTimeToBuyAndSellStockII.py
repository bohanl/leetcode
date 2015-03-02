class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        pmax = 0
        if not prices:
            return pmax

        for i in xrange(1,len(prices)):
            if prices[i] > prices[i-1]:
                pmax += prices[i]-prices[i-1]

        return pmax