"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # sort inbuilt method which takes an anonymous function as key
        intervals.sort(key=lambda i : i.start)
        for i in range(0,len(intervals)-1):
            firstInterval = intervals[i]
            secondInterval = intervals[i+1]
            if firstInterval.end > secondInterval.start:
                return False
        
        return True
