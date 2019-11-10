#leetcode 15
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]: #to select unique values for i
                continue
                
            j = i+1
            k = len(nums)-1
            
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s < 0:
                    j +=1
                    
                elif s > 0:
                    k -=1
                    
                else:
                    result.append((nums[i], nums[j], nums[k]))
                    while(j<k and nums[j] == nums[j+1]): # to get unique values for j and k
                        j +=1
                    while(j<k and nums[k] == nums[k-1]):
                        k -=1
                    j +=1
                    k -=1
                    
        return result
