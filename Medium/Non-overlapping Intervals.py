#Leetcode 435. Non-overlapping Intervals

class Solution1:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0]) #sort by start time
        count = 0
        currEnd = intervals[0][1]
        
        for i in range(1,len(intervals)):
            if intervals[i][0] < currEnd:
                count += 1
                currEnd = min(intervals[i][1], currEnd)
            else:
                currEnd = intervals[i][1]
        return count

class Solution2:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1]) #sort by end time
        count = 0
        currEnd = intervals[0][1]
        
        for i in range(1,len(intervals)):
            if intervals[i][0] < currEnd:
                count += 1
            else:
                currEnd = intervals[i][1]
        return count