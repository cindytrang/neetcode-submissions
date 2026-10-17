class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0]) # return based on the start O nlogn
        res = [intervals[0]]

        for start, end in intervals:
            lastEnd = res[-1][1]
            if start <= lastEnd:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start, end])
        return res
