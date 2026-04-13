class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        retList = []
        intervals.sort(key=lambda x: x[0])
        ind = -1

        for i in range(len(intervals)):
            interval = intervals[i]
            if i == 0:
                retList.append(interval)
                ind += 1
            
            # check if it overlaps if not append
            elif retList[ind][1] < interval[0]:
                retList.append(interval)
                ind += 1

            else:
                retList[ind][0]= min(retList[ind][0],interval[0])
                retList[ind][1] = max(retList[ind][1],interval[1])

        return retList
