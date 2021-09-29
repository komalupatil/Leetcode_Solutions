#Leetcode 477. Total Hamming Distance

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        total_hamming_dist = 0
        for i in range(32):
            ones = 0
            for num in nums:
                ones += (num >> i) & 1
            total_hamming_dist += ones * (len(nums) - ones)
        return total_hamming_dist