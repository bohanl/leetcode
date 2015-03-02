class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if not s:
            return 0
        
        n = len(s)

        dp = [0]*n
        dp[0] = 1 if s[0] != '0' else 0
        
        for i in xrange(1,n):
            dp[i] = dp[i-1] if s[i] != '0' else 0
            if s[i-1] == '1' or s[i-1] == '2':
                num = int(s[i-1:i+1])
                if num >= 10 and num <= 26:
                    dp[i] += dp[i-2] if i>1 else 1
        
        return dp[-1]
