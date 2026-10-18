from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_dict = {}
        for s in strs:
            character_occurences = frozenset(Counter(s).items())
            if character_occurences in grouped_dict:
                grouped_dict[character_occurences].append(s)
            else:
                grouped_dict[character_occurences] = [s]

        return list(grouped_dict.values())
