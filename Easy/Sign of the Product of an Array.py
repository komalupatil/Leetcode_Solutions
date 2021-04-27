#Leetcode 1822. Sign of the Product of an Array

class Solution1:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        product = 1
        for num in nums:
            product *= num
        if product < 0:
            return -1
        if product > 0:
            return 1
        if product ==0:
            return 0

class Solution2:
    def arraySign(self, nums: List[int]) -> int:
        sign = 1
        
        for num in nums:
            if num > 0:
                continue
            elif num == 0:
                return 0
            else:
                sign = sign * (-1)
        return sign

