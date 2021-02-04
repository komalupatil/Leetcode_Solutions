#Leetocde 35. Search Insert Position

#Solution - Binary Search (array is sorted)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) -1
        
        while l<=r:
            mid = (r+l)//2
            if target < nums[mid]:
                r = mid -1
            elif target >nums[mid]:
                l = mid+1
            else:
                return mid
        return l