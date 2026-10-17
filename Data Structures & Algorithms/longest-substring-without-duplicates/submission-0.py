class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            seen = {} 
            l, r = i, i
            while r < len(s):
                seen[s[r]] = seen.get(s[r], 0) + 1 
                if seen[s[r]] > 1: 
                    break
                r += 1
            sub_len = r - l
            res = max(sub_len, res)
        return res