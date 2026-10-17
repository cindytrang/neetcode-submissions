class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counts_t = {}
        counts_s = {}
        res = []
        for e in range(len(t)):
            counts_t[t[e]] = counts_t.get(t[e], 0) + 1

        for i in range(len(s)):
            counts_s = {}
            for j in range(i, len(s)):
                counts_s[s[j]] = counts_s.get(s[j], 0) + 1

                if all(counts_s.get(key, 0) >= counts_t[key] for key in counts_t):
                    res.append(s[i:j+1])
                    
        if not res:
            return ""
        min_str = res[0]
        for r in res:
            window = len(r)
            if len(r) < len(min_str):
                min_str = r
        
        return min_str