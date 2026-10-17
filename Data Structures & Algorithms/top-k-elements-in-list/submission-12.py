import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums: # 0n times 
            freq[num] = freq.get(num,0) + 1 # 01 lookup

        # use sorting algorimth 0nlong with minheap
        # heap = []

        # for num, count in freq.items(): # this iterates onlogn but why 
        #     heapq.heappush(heap, (count, num))
        #     if len(heap) > k:
        #         heapq.heappop(heap) # removes the min
                    
        # return [num for count, num in heap]

        #Use the bucket sort algorithm to create n buckets, grouping numbers based on their frequencies from 1 to n. Then, pick the top k numbers from the buckets, starting from n down to 1.
        buckets = [ [] for _ in range(len(nums)+1)]

        # Step 3: place numbers into buckets by frequency
        for num, count in freq.items():
            buckets[count].append(num)

        # Step 4: collect top k from high frequency → low
        res = []
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res

