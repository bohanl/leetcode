class Solution:
    def find_peak_element(self, num, p, q, n):
        r = (p+q)/2

        if (r == 0 or num[r] > num[r-1]) and (r == n-1 or num[r] > num[r+1]):
            return r
        elif r > 0 and num[r] < num[r-1]:
            return self.find_peak_element(num, p, r-1, n)
        else:
            return self.find_peak_element(num, r+1, q, n)

    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        n = len(num)
        p, q = 0, n-1
        return self.find_peak_element(num, p, q, n)