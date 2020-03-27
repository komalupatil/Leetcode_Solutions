#Leetcode 41. First Missing Positive

#solution1
#using set and extra space

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 1
        nums = set(nums)
        ans = 1
        while ans in nums:
            ans+=1
        return ans


#Solution2 using cyclic sort (O(n) time and o(1) space)

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 1
        i = 0
        while i < len(nums):
            if nums[i] <= 0 or nums[i] > len(nums):
                i +=1
                continue
            j = nums[i]-1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i+=1
            
        for i in range(len(nums)):
            if i+1 != nums[i]:
                return i+1
        return len(nums)+1
        
        
            
        
