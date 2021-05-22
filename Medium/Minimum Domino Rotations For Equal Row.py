#Leetcode 1007. Minimum Domino Rotations For Equal Row

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        topA = self.helper(A, B, A[0])
        botA = self.helper(B, A, A[0])
        topB = self.helper(A, B, B[0])
        botB = self.helper(B, A, B[0])
        m = min(topA, botA, topB, botB)
        return -1 if m==30000 else m
        
    def helper(self, top, bottom, match):
        count = 0
        for i in range(len(top)):
            if top[i] != match:
                if bottom[i] == match:
                    count +=1
                else:
                    return 30000
        return count