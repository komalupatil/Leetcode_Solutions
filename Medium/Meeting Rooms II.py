#Leetcode 253. Meeting Rooms II

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x:x[0])
        
        minRooms = 0
        minHeap = []
        
        for interval in intervals:
            while (len(minHeap) > 0 and interval[0] >= minHeap[0]):
                heapq.heappop(minHeap)
            
            heapq.heappush(minHeap, interval[1])
            
            minRooms = max(minRooms, len(minHeap))
            
        return minRooms