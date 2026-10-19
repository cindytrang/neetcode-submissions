import heapq
from collections import Counter 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # char_occurences = Counter(nums) # o(n)
        # max_count = [(-freq, char) for char, freq in char_occurences.items()]
        # heapq.heapify(max_count)
        # return [heapq.heappop(max_count)[1] for _ in range(k)]

        # better bucket sort instead
        counts = Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)]
        for char,freq in counts.items():
            buckets[freq].append(char)

        result = []
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
        return result