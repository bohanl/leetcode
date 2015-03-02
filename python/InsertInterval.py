# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)

        j = len(intervals)-1
        while j > 0 and intervals[j].start < intervals[j-1].start:
            intervals[j], intervals[j-1] = intervals[j-1], intervals[j]
            j -= 1

        res = [intervals[0]]
        for i in xrange(1,len(intervals)):
            if intervals[i].start <= res[-1].end:
                res[-1].end = max(res[-1].end, intervals[i].end)
            else:
                res.append(intervals[i])

        return res