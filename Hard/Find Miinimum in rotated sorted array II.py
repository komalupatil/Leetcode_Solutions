#leetcode 154
#         0 1 2 3 4 5 6  mid
#input =  [1,2,3,4,5,6,7] 3 = 4
#output = [7,1,2,3,4,5,6] 3 = 3
   #output = [6,7,1,2,3,4,5]
   #output = [5,6,7,1,2,3,4]
   #output = [4,5,6,7,1,2,3]
   #output = [3,4,5,6,7,1,2]
   #output = [2,3,4,5,6,7,1]
   #output = [1,2,3,4,5,6,7]


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while(left < right):
            mid = left + (right-left)//2
            if nums[mid] < nums[right]:  #means start to mid might have smaller numbers
                #mid to right has sorted elements in ascending order, so min can't be ahead of mid
                #it can be either mid or between start and mid - 1
                right = mid
            elif nums[mid] > nums[right]: #means start to mid has bigger numbers, and numbers after mid are smaller 
                #mid is bigger and start to mid is sorted - so min can't be there
                #so min should be between mid+1 to right
                left = mid + 1
            elif nums[mid] == nums[right]:
                right -= 1 #as its duplicate, go to next right, as we wont be able to find min if mid and high are both equal
        return nums[left]
