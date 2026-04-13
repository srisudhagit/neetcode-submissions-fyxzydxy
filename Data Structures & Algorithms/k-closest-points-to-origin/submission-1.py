class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # insert all points with dist as first element. 
        # remove only k elements from minheap
        minHeap = []
        for x,y in points:
            dist = x*x + y*y
            minHeap.append((dist, x, y))

        heapq.heapify(minHeap)
        res = []

        while k > 0:
            currdist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1

        return res
