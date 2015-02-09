class Solution:

    def _lcp_recursion(self, strs):
        if not strs or not strs[0]:
            return ''

        c = strs[0][0]

        for s in strs:
            if not s or s[0] != c:
                return ''

        return c + self.longestCommonPrefix([s[1:] for s in strs])

    def _lcp(self, strs):
        if not strs:
            return ''

        for i in xrange(len(strs[0])):
            for j in xrange(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return strs[0][0:i]

        return strs[0]

    # @return a string
    def longestCommonPrefix(self, strs):
        return self._lcp(strs)
