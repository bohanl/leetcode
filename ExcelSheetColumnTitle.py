class Solution:
    # @return a string
    def convertToTitle(self, num):
        s = ''
        while num:
            mod = True and num % 26 or 26
            s = chr(mod+64) + s
            num = (num-mod)/ 26

        return s