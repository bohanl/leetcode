class Solution:
    # @return a string
    def minWindow(self, S, T):
        n, m = len(S), len(T)
        if n < m: return ''

        found, needed = [0]*256, [0]*256
        for c in T: needed[ord(c)] += 1

        start, count, min_window = 0, 0, ''
        for end, sc in enumerate(S):
            p = ord(sc)
            # sc is not needed
            if needed[p] == 0: continue
            # needed and we haven't found all needed chars in S yet
            if found[p] < needed[p]: count += 1
            found[p] += 1
            if count != m: continue

            # when we get here, we know that we found at least all we need
            # and now it's a good time to try to minimize the window
            # move start point
            while start < end:
                p = ord(S[start])
                if needed[p] != 0:
                    # Can't go beyond this point since this is the minimal
                    # we need to maintain the window
                    if found[p] == needed[p]: break
                    found[p] -= 1
                start += 1

            # update result
            if not min_window or end-start+1 < len(min_window):
                min_window = S[start:end+1]

        return min_window
