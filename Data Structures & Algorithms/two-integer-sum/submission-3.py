from copy import copy

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums and target 
        remainder_nums = copy(nums) 

        for i, value in enumerate(nums):
            remainder_nums[i] = target - value
            if remainder_nums[i] in nums:
                for f, val in enumerate(nums):
                    if remainder_nums[i] == val and i != f:   
                        return list((i, f))
        
        return list()