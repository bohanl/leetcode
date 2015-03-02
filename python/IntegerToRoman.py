class Solution:
    SYMBOLS = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

    def get_symbol(self, n, symbols):
        if n == 0:
            return ''
        if n <= 3:
            return symbols[0]*n
        if n == 4:
            return symbols[0]+symbols[1]
        if n <= 8:
            return symbols[1]+symbols[0]*(n-5)
        return symbols[0] + symbols[2]

    # @return a string
    def intToRoman(self, num):
        assert num >= 1 and num <= 3999

        res, scale = '', 1000
        i = len(self.__class__.SYMBOLS)-1
        while i >= 0:
            n = num/scale
            res += self.get_symbol(n, self.__class__.SYMBOLS[i:])
            num, scale = num % scale, scale/10
            i -= 2
        return res
