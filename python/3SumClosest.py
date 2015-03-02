class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        i, n = 0, len(num)
        if n < 3:
            return 0

        res = sum(num[:3])
        num = sorted(num)

        while i < n-2:
            a = num[i]
            j, k = i+1, n-1
            while j < k:
                s = a + num[j] + num[k]

                if s == target: return target
                elif s < target: j += 1
                else: k -= 1
                
                if abs(res-target)>abs(s-target):
                    res = s

            while i<n-2 and num[i] == a: i+=1

        return res