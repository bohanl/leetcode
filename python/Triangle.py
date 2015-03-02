class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        s = [0] * len(triangle[-1])

        s[0] = triangle[0][0]

        for i in xrange(1, len(triangle)):
            s[i] = s[i-1] + row[-1]
            for j in range(i-1, 0, -1):
                s[j] = min(s[j], s[j-1]) + row[j]
            s[0] += row[0]

        return min(s)