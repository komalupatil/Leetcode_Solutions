#Leetcode 1099. Two Sum Less Than K

#Solution - using two pointers

class Solution:
    def twoSumLessThanK(self, nums, k):
        maximum = -1
        l, r = 0, len(nums)-1
        
        nums = sorted(nums)
        
        while (l < r):
            if (nums[l] + nums[r]) >= k:
                r -=1
            else:
                maximum = max(maximum, nums[l]+nums[r])
                l +=1
        return maximum

obj = Solution()
nums1 = [34,23,1,24,75,33,54,8]
k1 = 60
result1 = obj.twoSumLessThanK(nums1, k1)
print(result1)
A = [10,20,30]
K = 15
result2 = obj.twoSumLessThanK(A, K)
print(result2)
        
