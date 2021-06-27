#Leetcode 560. Subarray Sum Equals K


#TLE
class Solution1:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            add = 0
            for j in range(i, len(nums)):
                add += nums[j]
                if add == k:
                    count += 1
        return count

#Prefix Sum
#prefix_sum(i,j) = sum(0,j) - sum(0,i-1)
#k = sum(0,j) - sum(0,i-1)
#1,2,3   3
class Solution2:
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
                