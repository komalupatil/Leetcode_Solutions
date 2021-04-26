#Leetcode 961. N-Repeated Element in Size 2N Array

#Solution
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        d = {}
        for num in A:
            d[num] = d.get(num,0)+1
        for key,val in d.items():
            if val == len(A)//2:
                return key