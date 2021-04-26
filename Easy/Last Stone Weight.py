#Leetcode 1046. Last Stone Weight

#Solution using max heap
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 0:
            return 0
        h = [-1*i for i in stones]
        while len(h)>1:
            heapq.heapify(h)
            stone1 = heapq.heappop(h)
            stone2 = heapq.heappop(h)
            diff = stone1-stone2
            if diff == 0:
                continue
            else:
                heapq.heappush(h, diff)
        return -1*h[0] if h else 0