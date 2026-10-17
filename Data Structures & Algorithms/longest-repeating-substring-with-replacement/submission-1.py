class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        res = 0

        for i in range(n):
            count = {}
            max_freq = 0

            for j in range(i, n):
                count[s[j]] = count.get(s[j], 0) + 1
                max_freq = max(max_freq, count[s[j]])

                window_size =  j - i + 1
                replacements = window_size - max_freq
                if replacements <= k:
                    res = max(res, window_size)
        
        return res








