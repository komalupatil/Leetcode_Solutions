#Leetcode 560. Subarray Sum Equals K

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count,contSum = 0, 0        
        d = {}
        d[0] = 1 #taking this as contiguous sum start with 0
        
        for i in range(len(nums)):
            contSum += nums[i]
            if contSum-k in d:
                count += d[contSum-k] #difference between sum and k means that subarray exists
            if contSum in d:
                d[contSum] +=1
            else:
                d[contSum] = 1             
        return count                
                