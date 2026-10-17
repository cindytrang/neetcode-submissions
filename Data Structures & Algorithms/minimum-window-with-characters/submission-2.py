class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        t_counts = {}
        for char in t:
            t_counts[char] = t_counts.get(char, 0) + 1

        required = len(t_counts)
        satisfied = 0
        window_freq = {}
        left = 0
        best = ""

        for right in range(len(s)):
            window_freq[s[right]] = window_freq.get(s[right], 0) + 1

            if s[right] in t_counts and window_freq[s[right]] == t_counts[s[right]]:
                satisfied += 1
            
            while satisfied == required:
                current = s[left:right+1]
                if not best or len(current) < len(best):
                    best = current
                
                window_freq[s[left]] -= 1
                if s[left] in t_counts and window_freq[s[left]] < t_counts[s[left]]:
                    satisfied -= 1
                left += 1

        return best