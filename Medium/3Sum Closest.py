#Leetcode 16. 3Sum Closest

#Solution

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        minDifference = float('inf')
        
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            
            while j<k:
                s = nums[i] + nums[j] + nums[k]
                
                if s == target :
                    return s
                
                difference = target - s
                if abs(difference) < abs(minDifference):
                    minDifference = difference
                
                if s > target:
                    k -=1
                else:
                    j+=1
        return target - minDifference