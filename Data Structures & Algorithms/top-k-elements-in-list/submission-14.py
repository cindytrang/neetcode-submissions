import heapq
from collections import Counter 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        char_occurences = Counter(nums)
        # each nums will have an associates count value 
        max_count = [(-freq, char) for char, freq in char_occurences.items()]
        heapq.heapify(max_count)
        return [heapq.heappop(max_count)[1] for _ in range(k)]


