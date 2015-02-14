class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        if not s and not p:
            return True
        if not p:
            return False
        if not s:
            return len(p) >= 2 and p[1] == '*' and self.isMatch(s, p[2:])

        sn, pn = len(s), len(p)

        if p[-1] not in ('*', '.') and p[-1] != s[-1]:
            return False

        if pn == 1:
            return sn == 1 and (p[0] == '.' or s[0] == p[0])

        if p[1] != '*':
            return (p[0] == '.' or s[0] == p[0]) and self.isMatch(s[1:], p[1:])
        else:
            if p[0] != '.':
                i = 0
                while i < sn and s[i] == p[0]:
                    if self.isMatch(s[i:], p[2:]):
                        return True
                    i += 1
                return self.isMatch(s[i:], p[2:])
            else:
                for i in xrange(sn+1):
                    if self.isMatch(s[i:], p[2:]):
                        return True
                return False
