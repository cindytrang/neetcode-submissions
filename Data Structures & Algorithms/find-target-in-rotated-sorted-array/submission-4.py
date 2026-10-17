class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (r+l)//2
            if nums[m] == target:
                return m
            # left half is sorted
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]: # target in this half
                    r = m - 1
                else: # target not in this half
                    l = m + 1
            else: #right side is sorted nums[l] > nums[m]
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            
        return -1

