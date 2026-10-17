class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        
        if n1 > n2:          # <-- add this
            return False

        s1_frequency = {}
        window_sliding = {}
        
        for i in range(n1):
            s1_frequency[s1[i]] = s1_frequency.get(s1[i], 0)+1
            window_sliding[s2[i]] = window_sliding.get(s2[i], 0)+1

        if s1_frequency == window_sliding:
            return True

        for i in range(n1, n2):
            new_char = s2[i]
            window_sliding[new_char] = window_sliding.get(s2[i], 0)+1

            old_char = s2[i-n1]
            window_sliding[old_char] -= 1
            if window_sliding[old_char] == 0:
                del window_sliding[old_char]

            if window_sliding == s1_frequency:
                return True
        
        return False