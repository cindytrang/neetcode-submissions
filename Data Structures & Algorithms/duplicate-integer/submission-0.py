class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_nums = set(nums)
        print(set_nums)
        return len(set_nums) != len(nums)