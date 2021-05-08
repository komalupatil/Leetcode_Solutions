#Leetcode 1512. Number of Good Pairs

class Solution1:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            d[num] = d.get(num,0)+1
        
        result = 0
        
        for val in d.values():
            if val >1:
                result += (val*(val-1)//2)
        return result

class Solution2:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = {}
        result  = 0
        
        for num in nums:
            if num in d:
                result += d[num]
                d[num] += 1
            else:
                d[num] = 1
        return result