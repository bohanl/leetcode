class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        max_area, n = 0, len(height)

        for i in xrange(n-1,-1,-1):
            min_bar = height[i]
            if i == n-1 or height[i] > height[i+1]:
                for j in xrange(i, -1, -1):
                    min_bar = min(min_bar, height[j])
                    max_area = max(max_area, (i-j+1)*min_bar)

        return max_area