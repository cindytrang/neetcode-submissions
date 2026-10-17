from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []

        for i, num in enumerate(nums):
            while dq and nums[dq[-1]] <= num: # while there are entries and the last elemen is smaller than the current num
                dq.pop()
            dq.append(i) # add the index of the new bigger one 

            if dq[0] <= i - k: # index of the biggest is smaller than the index - k window so its value out of bound the numeber is out of the sliding window pop it 
                dq.popleft()

            if i>=k - 1: # if index is is bigger of the window size
                res.append(nums[dq[0]])

        return res
