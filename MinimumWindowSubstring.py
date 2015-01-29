class Solution:
    # @return a string
    def minWindow(self, S, T):
        m, n = len(S), len(T)
        if m < n:
            return ''

        needed, found = [0]*256, [0]*256
        for c in T:
            needed[ord(c)] += 1
        
        start, count = 0, 0
        mw_start, mw_end = -1, m
        for end, ec in enumerate(S):
            i = ord(ec)
            
            if needed[i] == 0:
                continue

            if found[i] < needed[i]:
                count += 1
            
            found[i] += 1

            if count != n:
                continue

            while start < end:
                j = ord(S[start])
                if needed[j] != 0:
                    if found[j] <= needed[j]:
                        break
                    found[j] -= 1
                start += 1

            if end-start < mw_end-mw_start:
                mw_start, mw_end = start, end

        if mw_start == -1:
            return ''
        else:
            return S[mw_start:mw_end+1]


if __name__ == '__main__':
    print(Solution().minWindow('aa', 'aa'))