#Leetcode 1207. Unique Number of Occurrences

#Solution1
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

#Solution2

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for i in arr:
            if i not in d:
                d[i] = 1
            d[i] += 1
        return len(d.values()) == len(set(d.values()))