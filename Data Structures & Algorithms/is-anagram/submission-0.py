class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # create a map od dict for the strings and compare if they are the same
        char_s = createMapping(s)
        char_t = createMapping(t)

        return char_s == char_t

def createMapping(s: str) -> dict:
    char_dict = {}
    for char in s:
        value = char_dict.get(char, 0)
        char_dict.update({
            char: value + 1
        })
    return char_dict

