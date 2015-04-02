class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        n, res = len(s), set([])

        cache = set([])
        for i in xrange(n-9):
            ss = s[i:i+10]
            if ss in cache and not ss in res:
                res.add(ss)
            else:
                cache.add(ss)
        return list(res)

