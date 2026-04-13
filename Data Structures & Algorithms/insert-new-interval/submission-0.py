class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        length = len(intervals)

        # part - 1 while all the intervals' end value is less than new interval's start
        while i < length and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # part - 2 while all the intervals' end value is greater than new interval start
        while i < length and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0],intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)

        # part - 3 where all the intervals from here have start values greater than endvalue of new interval
        while i < length:
            res.append(intervals[i])
            i += 1

        return res