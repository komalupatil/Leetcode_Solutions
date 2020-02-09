#Leetcode 18
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)-3):
            if (i> 0 and nums[i] == nums[i-1]): #check duplicates in i
                continue
            for j in range(i+1, len(nums)-2): # start j from i+1 
                if (j>i+1 and nums[j]==nums[j-1]): # check duplicates in j
                    continue
                k = j+1
                l = len(nums)-1
                while(k<l): # two sum pointers
                    s = nums[i] + nums[j] + nums[k] + nums[l]
                    if s < target:
                        k +=1
                    elif s> target:
                        l -=1
                    else: 
                        result.append((nums[i], nums[j], nums[k], nums[l]))
                        while(k<l and nums[k]==nums[k+1]):
                            k+=1
                        while(k<l and nums[l]==nums[l-1]):
                            l-=1
                        k+=1
                        l-=1
        return result
