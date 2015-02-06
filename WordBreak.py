class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        if not s: return False

        T = [False] * (len(s)+1)
        T[0] = True

        for i in xrange(1,len(T)):
            j = i-1
            while j >= 0:
                T[i] = T[j] and s[j:i] in dict
                if T[i]: break
                j -= 1

        return T[-1]