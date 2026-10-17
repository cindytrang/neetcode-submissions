class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([str(len(s)) + "#" + s for s in strs])


    def decode(self, s: str) -> List[str]:
        res, i  = [], 0
        # 4#neet#"code","love","you"]

        while i < len(s):
            j = i 
            while s[j] != "#":
                j += 1
            size = int(s[i:j])
            bit = s[j+1:j+size+1]
            res.append(bit)
            i = j + 1 + size

        return res
