#Leetcode 33. Search in Rotated Sorted Array

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        #[5,6,7,8,1,2,3,4]
        
        while l<=r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[l]:
                if target >= nums[l] and target < nums[mid]:
                    r = mid -1
                else:
                    l = mid + 1
            else:
                if  target <= nums[r] and target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid -1
        return -1

            