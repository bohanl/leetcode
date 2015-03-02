class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        res = []

        num = sorted(num)

        i, n = 0, len(num)
        while i < n-2:
            a = num[i]
            j, k = i+1, n-1
            while j < k:
                b, c = num[j], num[k]
                s = a + b + c
                if s == 0:
                    res.append((a, b, c))
                    j, k = j+1, k-1
                    while j < k and num[j] == b: j+=1
                    while j < k and num[k] == c: k-=1
                elif s < 0:
                    j += 1
                else:
                    k -= 1

            while i<n-2 and num[i] == a: i+=1

        return res