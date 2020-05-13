#Leetcode 540. Single Element in a Sorted Array


#Solution1 - O(n)

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] =1
        for k,v in d.items():
            if v == 1:
                return k
        
#Solution2 O(log(n)) and O(1) space - using binary search

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) -1
        
        while left < right:
            mid = left + (right-left)//2
            check_if_halves_are_even = (right - mid)%2 == 0
            if nums[mid] == nums[mid+1]:
                if check_if_halves_are_even:
                    left = mid + 2
                else:
                    right = mid -1
            elif nums[mid] == nums[mid-1]:
                if check_if_halves_are_even:
                    right = mid -2
                else:
                    left = mid + 1
            else:
                return nums[mid]
        return nums[left]