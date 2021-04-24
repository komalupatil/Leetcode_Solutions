#Leetcode 1167. Minimum Cost to Connect Sticks

#Solution
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heap = []
        for i in sticks:
            heapq.heappush(heap, i)
        
        result, temp = 0,0
        while len(heap) > 1:
            temp = heapq.heappop(heap) + heapq.heappop(heap)
            result += temp
            heapq.heappush(heap, temp)
        return result