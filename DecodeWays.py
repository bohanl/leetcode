class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if len(s) < 2:
            return 1

        a1, a2 = 1, 1
        for i in xrange(1,len(s)):
            a1, c = a2, s[i]
            if c < '0' or c > '9': return 0
            if s[i-1] != '0' and int(s[i-1:i+1]) <= 26:
                a2 = a1 + a2
            else:
                a2 = a1

        return a2
