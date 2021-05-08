#Leetcode 1464. Maximum Product of Two Elements in an Array

class Solution1:
    def maxProduct(self, nums: List[int]) -> int:
        a,b = float('-inf'), float('-inf')
        
        for num in nums:
            if num>a:
                a,b = num,a
            elif num>b:
                b = num
        return (a-1)*(b-1)

class Solution2:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1]-1)*(nums[-2]-1)