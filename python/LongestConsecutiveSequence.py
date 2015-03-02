class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        if not num: return 0

        s = set(num)
        i, lcs = 0, 0

        while i < len(num) and s:
            count, x = 1, num[i]
            up, down = x+1,x-1

            while up in s:
                s.remove(up)
                count += 1
                up += 1

            while down in s:
                s.remove(down)
                count += 1
                down -= 1

            i += 1
            lcs = max(lcs, count)

        return lcs