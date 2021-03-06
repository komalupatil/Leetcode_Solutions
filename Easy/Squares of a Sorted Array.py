#Solution1 o(nlog(n))
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(i**2 for i in A)


#leetcode 977
#o(n) solution usig two pointers
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        if len(A) == 1:
            return [A[0]*A[0]]
        t = [0] * len(A)
        p1 = 0
        p2 = len(A) -1
        for i in range(len(A)-1, -1, -1):
                if abs(A[p1]) > abs(A[p2]): 
                    t[i] = A[p1] ** 2
                    p1 += 1
                else:
                    t[i] = A[p2] ** 2
                    p2 -= 1

        return t
