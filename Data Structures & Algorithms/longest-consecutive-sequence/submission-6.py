class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            # start of the sequence then length is 0
            if (n-1) not in numSet:
                length = 0 
                # since this is the start number we check all the sequences for the number
                while (n+length) in numSet:
                    length += 1 # conitnue the loop till we find it 
                # at the end we create the ,ac
                longest = max(length, longest)
        return longest