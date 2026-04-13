class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # get the frequency map of tasks and add frequency to maxheap and heapify
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        # create a doubly ended queue with pairs [-count, ideltimetowait]
        time = 0
        queue = deque() 

        while maxHeap or queue:
            time += 1
            if maxHeap:
                currentCount = 1 + heapq.heappop(maxHeap) 
                if currentCount:
                    queue.append([currentCount, time+n])

            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])
            
        return time

            

