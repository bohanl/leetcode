class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        aux = 1

        for i in xrange(len(digits)-1,-1,-1):
            d = digits[i]
            aux, digits[i] = (d + aux) / 10, (d + aux) % 10

        if aux:
            digits.insert(0, aux)
        
        return digits