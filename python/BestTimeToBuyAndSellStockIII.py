class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if not prices or len(prices) < 2:
            return 0

        n = len(prices)
        T, min_val = [0]*n, prices[0]

        for i in xrange(1,n):
            T[i] = max(T[i-1], prices[i]-min_val)
            min_val = min(min_val, prices[i])

        max_val, max_right, max_profit = prices[-1], 0, 0
        for i in xrange(n-1,-1,-1):
            max_profit = max(max_profit, T[i]+max_right)
            max_right = max(max_right, max_val-prices[i])
            max_val = max(max_val, prices[i])

        return max_profit