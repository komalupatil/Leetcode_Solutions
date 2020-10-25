#Leetcode 759. Employee Free Time

"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        heap = []
        for emp in schedule:
            for i in emp:
                heap.append((i.start, i.end))
        heapify(heap)
        
        s,e = heappop(heap)
        free = e
        result = []
        
        while heap:
            s,e = heappop(heap)
            if free < s:
                result.append(Interval(free, s))
                free = e
            else:
                free = max(free, e)
        return result