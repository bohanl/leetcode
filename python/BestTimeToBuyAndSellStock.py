class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if not prices:
            return 0

        min_val, max_profit = prices[0], 0
        for i in xrange(1, len(prices)):
            min_val = min(min_val, prices[i])
            max_profit = max(max_profit, prices[i]-min_val)

        return max_profit
