class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        res = []

        num = sorted(num)

        n = len(num)

        for i1 in xrange(n-3):
            if i1 > 0 and num[i1] == num[i1-1]: continue
            i2 = i1 + 1
            for i2 in xrange(i1+1, n-2):
                if i2 > i+1 and num[i2] == num[i2-1]: continue
                i3, i4 = i2+1, n-1
                while i3 < i4:
                    s = num[i1]+num[i2]+num[i3]+num[i4]
                    if s == target:
                        res.append([num[i1],num[i2],num[i3],num[i4]])
                        while i3 < i4 and num[i3+1] == num[i3]: i3 += 1
                        while i3 < i4 and num[i4-1] == num[i4]: i4 -= 1
                        i3, i4 = i3+1, i4-1
                    elif s > target:
                        i4 -= 1
                    else:
                        i3 += 1

        return res
