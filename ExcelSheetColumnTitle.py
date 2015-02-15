class Solution:
    # @return a string
    def convertToTitle(self, num):
        assert num > 0

        q = collections.deque([])
        while num:
            mod = True and num % 26 or 26
            q.appendleft(chr(mod+64))
            num = (num-mod)/ 26

        return ''.join(q)