class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        n = len(num)
        if n < 2: return 0

        a, b = min(num), max(num)
        m = (b-a)/n+1
        buckets = [None]*((b-a)/m+1)

        for x in num:
            i = (x-a)/m
            if buckets[i]:
                buckets[i][0] = min(buckets[i][0], x)
                buckets[i][1] = max(buckets[i][1], x)
            else:
                buckets[i] = [x, x]

        res, j = 0, 0
        for i in xrange(1, len(buckets)):
            if not buckets[i]: continue
            res = max(res, buckets[i][0]-buckets[j][1])
            j = i

        return res
