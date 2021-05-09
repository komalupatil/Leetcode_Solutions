class Solution:
    def max_sum_subarrays(self,nums,k):
        windowSum = 0
        maxSum = 0
        windowStart = 0
        for windowEnd in range(len(nums)):
            windowSum += nums[windowEnd]
            if windowEnd >= k-1:
                maxSum = max(maxSum, windowSum)
                windowSum -= nums[windowStart]
                windowStart += 1
        return maxSum
solution = Solution()
nums1= [1,12,-5,-6,50,3]
k1 = 3
result = solution.max_sum_subarrays(nums1, k1)
print(result)
Input=[2, 1, 5, 1, 3, 2]
k=3
result1 = solution.max_sum_subarrays(Input, k)
print(result1)
Input2=[2, 3, 4, 1, 5]
k2=2
result2 = solution.max_sum_subarrays(Input2, k2)
print(result2)


        
