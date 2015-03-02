class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        if not s or len(s) < 2:
            return 0
        
        n = len(s)
        T, longest = [0]*(n+1), 0
        for i in xrange(2, n+1):
            if s[i-1] == '(':
                continue
            j = i-2-T[i-1]
            if j >= 0 and s[j] == '(':
                T[i] = 2+T[i-1]+T[j]
                longest = max(longest, T[i])

        return longest        