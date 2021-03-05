#Leetcode 1748. Sum of Unique Elements

#Solution 

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        result = 0
        d = {}
        
        for num in nums:
            d[num] = d.get(num,0)+1
        
        for key,val in d.items():
            if val == 1:
                result +=key
        return result