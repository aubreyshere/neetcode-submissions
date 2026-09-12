"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        time = []
        rooms = 0
        maxRooms = 0

        for interval in intervals:
            time.append((interval.start, 1))
            time.append((interval.end, -1))
        time.sort(key=lambda x: (x[0], x[1]))

        for i, j in time:
            rooms += j
            maxRooms = max(maxRooms, rooms)

        return maxRooms
