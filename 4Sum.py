class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        res = []

        num = sorted(num)

        i1, n = 0, len(num)

        while i1 < n-3:
            a = num[i1]
            i2 = i1 + 1
            while i2 < n-2:
                b = num[i2]
                i3, i4 = i2+1, n-1
                while i3 < i4:
                    c, d = num[i3], num[i4]
                    s = a + b + c + d
                    if s == target:
                        res.append([a, b, c, d])
                        i3, i4 = i3+1, i4-1
                        while i3 < i4 and num[i3] == c: i3 += 1
                        while i3 < i4 and num[i4] == d: i4 -= 1
                    elif s > target:
                        i4 -= 1
                    else:
                        i3 += 1

                i2 += 1
                while i2 < n-2 and num[i2] == b: i2 += 1

            i1 += 1
            while i1 < n-3 and num[i1] == a: i1 += 1

        return res
