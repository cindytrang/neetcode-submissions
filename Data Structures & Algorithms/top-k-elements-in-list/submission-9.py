import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums: # 0n times 
            freq[num] = freq.get(num,0) + 1 # 01 lookup

        # use sorting algorimth 0nlong with minheap
        heap = []
        # iterate the frequency
        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap) # removes the min
                    
        return [num for count, num in heap]


            