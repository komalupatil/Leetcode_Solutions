#leetcode 34
#Find First and Last Position of Element in Sorted Array
#do binary search twice
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearchLeft(nums1, target1):
            left, right = 0, len(nums1) - 1
            while left <= right:
                mid = left + right - left // 2
                if target1 > nums1[mid]: 
                    left = mid + 1
                else: 
                    right = mid - 1
            return left

        def binarySearchRight(nums2, target2):
            left, right = 0, len(nums2) - 1
            while left <= right:
                mid = left + right - left // 2
                if target2 >= nums2[mid]: 
                    left = mid + 1
                else: 
                    right = mid - 1
            return right
        
        left, right = binarySearchLeft(nums, target), binarySearchRight(nums, target)
        return (left, right) if left <= right else [-1, -1]
            
            
        
