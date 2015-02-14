class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        if not p:
            return not s

        if len(p) > 1 and p[1] == '*':
            while s and (s[0] == p[0] or p[0] == '.'):
                if self.isMatch(s, p[2:]):
                    return True
                s = s[1:]
            return self.isMatch(s, p[2:])

        return (s and (s[0] == p[0] or p[0] == '.')) and \
                self.isMatch(s[1:], p[1:])