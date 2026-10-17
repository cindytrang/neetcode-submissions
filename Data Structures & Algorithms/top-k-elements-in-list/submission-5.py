class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_nums = {}
        set_results = []
        count = 0 
        most_frequent = defaultdict(list)
        
        while count < len(nums): # occurence list
            occurence = map_nums.get(nums[count], 0) + 1
            map_nums[nums[count]] = occurence
            count += 1
    
        for i in map_nums: # most frequent
            most_frequent[map_nums[i]].append(i)
        occurences = sorted(list(map_nums.values()))
        
        for i in range(k):
            max_occurence = occurences.pop()
            value = most_frequent[max_occurence].pop()
            set_results.append(value)
            

        return set_results
