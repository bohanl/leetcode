class Solution:
    # @return a string
    def minWindow(self, S, T):
        m, n = len(S), len(T)
        if m < n: return ''

        needed, found = [0]*256, [0]*256
        for c in T: needed[ord(c)] += 1
        
        start, count, min_window = 0, 0, ''
        for end, ec in enumerate(S):
            i = ord(ec)
            if needed[i] == 0:
                continue
            if found[i] < needed[i]:
                count += 1
            found[i] += 1
            if count != n:
                continue
            # move start
            while start < end:
                j = ord(S[start])
                if needed[j] != 0:
                    if found[j] <= needed[j]:
                        break
                    found[j] -= 1
                start += 1
            # update result
            if not min_window or end-start+1 < len(min_window):
                min_window = S[start:end+1]

        return min_window