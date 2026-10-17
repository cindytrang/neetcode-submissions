class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use bucket sort instead but bounded by the length of the nums 

        # count the occurances
        occurance = {}
        freq = [[] for i in range(len(nums)+1)]

        for num in nums:
            occurance[num] = occurance.get(num, 0) + 1
        for n, c in occurance.items():
            freq[c].append(n)

        res = []

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

    