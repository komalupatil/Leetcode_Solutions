#Leetcode 287. Find the Duplicate Number
 
class Solution1:
    def findDuplicate(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            d[num] = d.get(num,0)+1
        for key in d.keys():
            if d[key] > 1:
                return key

#https://leetcode.com/problems/find-the-duplicate-number/discuss/358670/BS-BinarySearch-with-very-detailed-explanation
class Solution2:
    def findDuplicate(self, nums: List[int]) -> int:
        low = 1
        high = len(nums) - 1
        
        while low<= high:
            mid = low + (high-low)//2
            eq= 0
            inRange = 0
            for i in range(len(nums)):
                if nums[i] == mid:
                    eq += 1
                    inRange += 1
                elif mid > nums[i] >= low:
                    inRange += 1
            if eq > 1:
                return mid
            elif inRange > mid -low + 1:
                high = mid - 1
            else:
                low = mid + 1
        return -1