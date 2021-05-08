#Leetcode 454. 4Sum II

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        table = {}
        
        for a in A:
            for b in B:
                table[a+b] = table.get(a+b,0)+1
        
        count = 0
        for c in C:
            for d in D:
                if (0-c-d) in table:
                    count += table[0-c-d]
        return count