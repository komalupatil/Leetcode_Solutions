#Leetcode 905. Sort Array By Parity

class Solution1:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        if len(A) == 0:
            return 0
        p1 = 0
        p2 = len(A)-1
        while p1<p2:
            if A[p1]%2==0:
                p1+=1
                continue
            if A[p2]%2!=0:
                p2-=1
                continue
            if p1<p2:
                A[p1], A[p2] = A[p2], A[p1]
                p1+=1
                p2-=1
        return A
            
class Solution2:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        if len(A) == 0:
            return 0
        p1 = 0
        p2 = len(A)-1
        while p1<=p2:
            if A[p1]%2==0:
                p1+=1
            else:
                A[p1], A[p2] = A[p2], A[p1]
                p2-=1
        return A