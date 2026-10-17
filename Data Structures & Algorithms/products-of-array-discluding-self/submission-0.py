class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1


        res = [1 for i in range(len(nums))]
        prefix = [1 for i in range(len(nums))]
        postfix = [1 for i in range(len(nums))]

        #get prefix:
        for i, val in enumerate(nums):
            if i < 1:
                prefix[0] = val
            prefix[i] = prefix[i-1] * val

        print(prefix)
            

        #get prefix:
        for i in range(len(nums) - 1, - 1, -1):
            if i == len(nums) - 1:
                postfix[i] = nums[i]
            else:
                postfix[i] = postfix[i+1] * nums[i]

        print(postfix)

        for i, val in enumerate(nums):
            if i < 1:
                res[i] = postfix[i+1]
            elif i + 2 > len(nums):
                res[i] = prefix[i-1]
            else:
                res[i] = prefix[i-1] * postfix[i+1]

            
        return res
        