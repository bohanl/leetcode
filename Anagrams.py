class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        res = []
        if not strs: return res

        d = {}
        for i, s in enumerate(strs):
            ss = ''.join(sorted(s))
            if d.has_key(ss):
                d[ss].append(i)
            else:
                d[ss] = [i]
        
        for k, v in d.items():
            if len(v) > 1:
                res.extend([strs[i] for i in v])
        
        return res