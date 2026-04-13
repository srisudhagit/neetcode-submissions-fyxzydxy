class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # approach using built in functions
        #numsCounter = Counter(nums)
        #topk_elements = numsCounter.most_common(k)
        
        #return [num for num ,cnt in topk_elements]

        freqList = []
        eleFreqMap = {}
        #create map of element ans its frequency
        for num in nums:
            eleFreqMap[num] = 1 + eleFreqMap.get(num,0)

        # create priority min heap to pick smallest frequency each time when length exceeds K
        heap = []
        for num in eleFreqMap.keys():
            heapq.heappush(heap, (eleFreqMap[num] , num))
            # removes lowest frequent number and only top K remains
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res


        