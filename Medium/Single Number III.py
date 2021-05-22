#Leetcode 260. Single Number III

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d = {}
        result = []
        for i in nums:
            if i in d:
                d[i] +=1
            else:
                d[i] = 1
        print(d)
                
        for k in d.keys():
            if d[k] == 1:
                result.append(k)
        
        return result