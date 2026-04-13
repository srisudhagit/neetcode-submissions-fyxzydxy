"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        minHeap = []
        intervals.sort(key = lambda x:x.start)
        maxlen = 0

        for i,interval in enumerate(intervals):

            while minHeap and minHeap[0] <= interval.start:
                heapq.heappop(minHeap)
            
            heapq.heappush(minHeap, interval.end)

            maxlen = max(maxlen, len(minHeap))

        return maxlen

        