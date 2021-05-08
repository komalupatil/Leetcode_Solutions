#Leetcode 1337. The K Weakest Rows in a Matrix
 
from heapq import nsmallest 
class Solution1:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        S = [[sum(g),i] for i,g in enumerate(mat)]
        return (i for count, i in nsmallest(k,S) )

class Solution2:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        S = [[sum(g),i] for i,g in enumerate(mat)]
        R = sorted(S)
        return [r[1] for r in R[:k]]