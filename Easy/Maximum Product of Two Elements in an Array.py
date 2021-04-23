#Leetcode 1464. Maximum Product of Two Elements in an Array

#Solution1
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a,b = float('-inf'), float('-inf')
        
        for num in nums:
            if num>a:
                a,b = num,a
            elif num>b:
                b = num
        return (a-1)*(b-1)

#Solution2
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1]-1)*(nums[-2]-1)