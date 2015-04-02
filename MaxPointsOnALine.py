class Solution:

    def _same_points(self, p1, p2):
        return p1.x == p2.x and \
               p1.y == p2.y

    def _get_slope(self, p1, p2):
        x1, y1, x2, y2 = p1.x, p1.y, p2.x, p2.y
        if x1 != x2: return 1.0 * (y1-y2) / (x1-x2)
        else: float('inf')

    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        if not points:
            return 0

        n = len(points)

        max_points = 1

        for i in xrange(n-1):
            d = {}
            max_points_local, same_points = 1, 0
            for j in xrange(i+1,n):
                if self._same_points(points[i], points[j]):
                    same_points += 1
                    continue
                slope = self._get_slope(points[i], points[j])
                d[slope] = d.get(slope, 1)+1
                max_points_local = max(max_points_local, d[slope])

            max_points = max(max_points, max_points_local+same_points)

        return max_points