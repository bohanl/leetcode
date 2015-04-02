class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        if not strs: return []

        res, d = [], {}
        for i, s in enumerate(strs):
            ss = ''.join(sorted(s))
            d.get(ss, []).append(i)

        for k, v in d.items():
            if len(v) > 1:
                res.extend([strs[i] for i in v])

        return res