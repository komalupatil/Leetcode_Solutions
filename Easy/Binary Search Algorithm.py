#leetcode 704
#time complexity log2(n) +1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) -1
        while(start <= end):
            mid = start + (end-start)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid -1
            else:
                start = mid+1
        return -1
