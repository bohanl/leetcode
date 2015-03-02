class Solution:
    # @return an integer
    def maxArea(self, height):
        if not height or len(height) < 2:
            return 0

        i, j, max_area = 0, len(height)-1, 0

        while i < j:
            h1, h2 = height[i], height[j]
            max_area = max(max_area, min(h1, h2)*(j-i))
            if h2 >= h1:
                i += 1
            else:
                j -= 1

        return max_area