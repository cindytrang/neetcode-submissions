class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, current, total):
            if total == target:
                res.append(current.copy())
                return
            
            if total > target:
                return

            for i in range(start, len(nums)):
                value = nums[i]
                current.append(value)
                backtrack(i, current, total+value)
                current.pop()

            
        backtrack(0, [], 0)
        return res