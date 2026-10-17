class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        res = []
        for i in range(0,len(nums)):
            heapq.heappush(max_heap,(-nums[i], i))
            while max_heap[0][1] <= i - k:
                heapq.heappop(max_heap)
                
            if i  >= k - 1:
                res.append(-max_heap[0][0])
        return res
                
