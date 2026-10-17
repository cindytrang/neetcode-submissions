"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = defaultdict(int)

        for i in intervals:
            events[i.start] += 1
            events[i.end] -= 1

        max_events = 0
        active_meetings = 0 
        for event, counts in sorted(events.items()):
            active_meetings += counts
            max_events = max(max_events, active_meetings)
        return max_events

