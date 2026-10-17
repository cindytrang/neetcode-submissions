class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        #we iterate through the left and right 
        #area would be max(l, r) and then r-l 

        # complication we want to iterate through each combination 
        for i, a in enumerate(heights):
            l, r = i, len(heights)-1
            while l<r:
                print((min(l, r)),(r-l))
                area = (min(heights[l], heights[r])) * (r-l)
                maxArea = max(maxArea, area)
                r -= 1
        return maxArea