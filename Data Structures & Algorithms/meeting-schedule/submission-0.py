"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        lastEnd = -1
        intervals.sort(key=lambda i: i.start)

        for interval in intervals:
            if interval.start >= lastEnd:
                lastEnd = interval.end
            else:
                return False

        return True
