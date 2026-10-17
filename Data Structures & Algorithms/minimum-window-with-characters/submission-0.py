class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counts_t = {}
        res = []
        for e in range(len(t)):
            counts_t[t[e]] = counts_t.get(t[e], 0) + 1

        counts_s = {}
        for i in range(len(s)):
            temp = counts_t.copy()
            for j in range(i, len(s)):
                if s[j] in temp:
                    temp[s[j]] -= 1
                    if temp[s[j]] == 0:
                        del temp[s[j]]
                if not temp:
                    res.append(s[i:j+1])
                    break
        res=min(res, key=len) if res else ""
        return res