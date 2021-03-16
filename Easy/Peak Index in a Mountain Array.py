#Leetcode 852. Peak Index in a Mountain Array

#Solution - binary search

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        h = len(arr) -1
        ans = 0
        
        while l<= h:
            mid = l+(h-l)//2
            if arr[mid-1] < arr[mid] > arr[mid+1]:
                ans = mid
                break
            elif arr[mid-1] < arr[mid] < arr[mid+1]:
                l = mid+1
            else:
                h = mid -1
        return ans