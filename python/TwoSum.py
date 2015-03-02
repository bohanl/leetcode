class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        d = {}
        for i, x in enumerate(num):
            y = target-x
            if d.has_key(y):
                return (d[y]+1, i+1)
            d[x] = i
        
        return None