#Leetcode 1167. Minimum Cost to Connect Sticks

mport heapq
class Solution:
    def connectSticks(self, sticks):
        heap = []
        for i in sticks:
            heapq.heappush(heap, i)

        result, temp = 0,0
        while len(heap) > 1:
            temp = heapq.heappop(heap) + heapq.heappop(heap)
            result += temp
            heapq.heappush(heap, temp)
        return result

solution = Solution()
Sticks = [2,4,3]
print(solution.connectSticks(Sticks))