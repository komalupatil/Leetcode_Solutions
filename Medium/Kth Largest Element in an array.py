#Leetcode 215. Kth Largest Element in an array
# 
# Solution using min heap
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        for _ in range(len(nums)-k):
            heapq.heappop(heap)
        return heapq.heappop(heap)

#Solution - maxHeap
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for num in nums:
            heapq.heappush(h,-num)
        for _ in range(k-1):
            heapq.heappop(h)
        return -1 *heapq.heappop(h)
