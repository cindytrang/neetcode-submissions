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
            
            # 3 4
            # 2 3
            # 5 2
            # 6 1

        
        return list()