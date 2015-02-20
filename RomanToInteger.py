class Solution:
    RI_MAP = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    # @return an integer
    def romanToInt(self, s):
        if not s: return 0

        res = self.__class__.RI_MAP[s[0]]
        for i in xrange(1,len(s)):
            prev, curr = self.__class__.RI_MAP[s[i-1]], self.__class__.RI_MAP[s[i]]
            res += curr
            if curr > prev:
                res -= 2*prev

        return res