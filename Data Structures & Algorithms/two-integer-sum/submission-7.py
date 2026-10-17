from copy import copy

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, val in enumerate(nums):
            to_find = target - val
            if to_find in seen:
                return [seen.get(to_find), i]
            seen[val] = i


        # so now we have a map with the seen values and their indexes 
        #map of seen values 