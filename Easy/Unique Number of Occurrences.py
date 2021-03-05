#Leetcode 1207. Unique Number of Occurrences

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        res = []
        
        for num in arr:
            d[num] = d.get(num,0)+1
            
        for val in d.values():
            if val in res:
                return False
            else:
                res.append(val)
        return True