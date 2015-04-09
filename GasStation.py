class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        rsum, total, j = 0, 0, -1

        for i, g in enumerate(gas):
            d = g-cost[i]
            rsum, total = rsum+d, total+d
            if rsum < 0:
                rsum, j = 0, i

        if total < 0: return -1
        return j+1
