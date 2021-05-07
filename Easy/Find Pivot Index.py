#Leetcode 724. Find Pivot Index

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        weight_on_left = 0
        weight_on_right = sum(nums)
        
        for i, wt in enumerate(nums):
            weight_on_right -= wt
            
            if weight_on_left == weight_on_right:
                return i
        
            else:
                weight_on_left += wt
        return -1