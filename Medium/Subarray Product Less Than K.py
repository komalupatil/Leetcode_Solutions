#Leetcode 713. Subarray Product Less Than K

#Solution
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        product = 1
        count = 0
        
        for right in range(len(nums)):
            product *= nums[right]
            while product >= k and left <=right:
                product /= nums[left]
                left += 1
            count += right-left + 1
        return count