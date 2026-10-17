class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # group all anagrams into sublist 
        sorted_map = {}
        sets = []
        if len(strs) == 1:
            sets.append(strs)
            return sets

        #enumarate all strings that O(m)
        for i, word in enumerate(strs): 
            sorted_chars = ''.join(sorted(word))
            if sorted_chars in sorted_map:
                sorted_map[sorted_chars].append(word)
            else:
                sorted_map[sorted_chars] = [word]
                
        return list(sorted_map.values())





