class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1, 2, 4 target = 3
        l, r = 0, len(nums) -1
        mid = len(nums)//2

        while l<= r:
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
            mid = (l + r) // 2

        return -1