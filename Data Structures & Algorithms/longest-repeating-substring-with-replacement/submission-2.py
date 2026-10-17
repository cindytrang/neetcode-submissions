class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # replace the least freq
        # replacements = length of the valid string - the freq of the most frequent 
        # if valid we would take that string
        res = 0 
        for i in range(len(s)):
            max_freq = 0
            count = {}
            for j in range(i, len(s)):
                count[s[j]] = count.get(s[j], 0) + 1
                max_freq = max(max_freq, count[s[j]])
                window_size = j - i + 1 
                replacements = window_size - max_freq
                if replacements <= k:
                    #valid string
                    res = max(res, window_size)
        return res







