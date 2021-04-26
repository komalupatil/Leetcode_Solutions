#Leetcode 896. Monotonic Array

#Solution
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) == 0:
            return True
        
        isIncreasing = True
        isDecreasing = True
        
        for i in range(1, len(A)):
            if A[i] < A[i-1]:
                isIncreasing = False
            if A[i] > A[i-1]:
                isDecreasing = False
        
        return isIncreasing or isDecreasing