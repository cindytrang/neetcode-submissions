class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        n = len(height)

        res = 0 
        maxLeft = [0] * n
        maxRight = [0] * n

        maxLeft[0] = height[0]
        for i in range(1, n):
            maxLeft[i] = max(height[i], maxLeft[i-1])
        
        maxRight[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            maxRight[i] = max(height[i], maxRight[i+1])


        for i in range(1,n):
            res += max(0,(min(maxLeft[i], maxRight[i]) - height[i]))
        
        return res
            



        
                



        