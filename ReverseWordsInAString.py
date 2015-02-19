class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        j, res = len(s), []
        for i in xrange(len(s)-1,-1,-1):
            if s[i] == ' ':
                j = i
            elif i == 0 or s[i-1] == ' ':
                res.append(s[i:j])

        return ' '.join(res)