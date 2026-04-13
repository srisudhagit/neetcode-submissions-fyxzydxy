"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key = lambda x:x.start)

        roomslist = []

        heapq.heappush(roomslist,intervals[0].end)

        for interval in intervals[1:]:
            # check if current interval is can be included in the room. If so pop, and enter current interval end
            if interval.start >= roomslist[0]:
                heapq.heappop(roomslist)
            heapq.heappush(roomslist,interval.end)
        
        return len(roomslist)