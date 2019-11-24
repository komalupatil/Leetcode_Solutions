#leetcode 189
class Solution:
    #reverse function
    def rev(self, nums, s, e):
            while(s < e):
                temp = nums[s]
                nums[s] = nums[e]
                nums[e] = temp
                s +=1
                e -=1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k% len(nums)
        #use reverse function to rotate elements
        self.rev(nums, 0, len(nums)-1)
        self.rev(nums, 0, k-1)
        self.rev(nums, k, len(nums)-1)
