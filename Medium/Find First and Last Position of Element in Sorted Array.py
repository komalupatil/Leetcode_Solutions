#Leetcode 34. Find First and Last Position of Element in Sorted Array

#do binary search twice
class Solution1:
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
        
#follow (https://leetcode.com/discuss/general-discussion/1089533/An-approach-to-writing-bug-free-Binary-Search-code)        
class Solution2:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def findFirst(nums, target):
            l = 0
            h = len(nums)-1
            ans = -1
            while l<=h:
                mid = l+ (h-l)//2
                if nums[mid] == target:
                    ans = mid
                    h = mid - 1
                elif nums[mid] > target:
                    h = mid - 1
                else:
                    l = mid + 1
            return ans
        def findLast(nums, target):
            l = 0
            h = len(nums)-1
            ans = -1
            while l<=h:
                mid = l + (h-l)//2
                if nums[mid] == target:
                    ans = mid
                    l = mid + 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    h = mid - 1
            return ans
        
        result = [-1, -1]
        result[0] = findFirst(nums, target)
        result[1] = findLast(nums, target)
        return result