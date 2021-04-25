#Leetcode 989. Add to Array-Form of Integer

#Solution1
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        final_list = []
        output = str(int("".join(map(str, A))) + K)
        for i in output:
            final_list.append(int(i))
        return final_list

#Solution2
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        A[-1] += K
        i = len(A) - 1
        while i > 0 and A[i] > 9:
            A[i-1] += A[i] // 10
            A[i] = A[i] % 10
            i -= 1
        print(A)
        while A[0] > 9:
            A = [A[0] // 10] + A
            A[1] = A[1] % 10
        return A