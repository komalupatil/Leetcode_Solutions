#Leetcode 1383. Maximum Performance of a Team


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = list(zip(efficiency, speed))
        print(engineers)
        engineers.sort(reverse=True)  # Sort by decreasing order of efficiency
        print(engineers)
        minHeap = []
        speedSum = 0
        ans = 0
        for e, s in engineers:
            speedSum += s
            heappush(minHeap, s)
            print(minHeap)
            if len(minHeap) > k:  # Over k engineers -> remove the lowest speed engineer
                speedSum -= heappop(minHeap)
            print(speedSum)
            ans = max(ans, speedSum * e)
        return ans % (10**9 + 7)