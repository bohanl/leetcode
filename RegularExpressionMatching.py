class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        if not p:
            return not s

        if len(p) > 1 and p[1] == '*':
            i = 0
            while i < len(s) and (s[i] == p[0] or p[0] == '.'):
                if self.isMatch(s[i:], p[2:]): return True
                i += 1
            return self.isMatch(s[i:], p[2:])

        return (len(s) and (s[0] == p[0] or p[0] == '.')) and self.isMatch(s[1:], p[1:])