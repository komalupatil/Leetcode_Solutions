#Leetcode 1002. Find Common Characters

from collections import Counter
class Solution1:
    def commonChars(self, A: List[str]) -> List[str]:
        
        counter1 = Counter(A[0])
        
        for a in A[1:]:
            counter2 = Counter(a)
            for k in counter1.keys():
                counter1[k] = min(counter1[k], counter2[k])
        return counter1.elements()

class Solution2:
    def commonChars(self, A: List[str]) -> List[str]:
        
        counter1 = collections.Counter(A[0])
        
        for a in A[1:]:
            counter1 &= Counter(a)
        return list(counter1.elements())

class Solution3:
    def commonChars(self, A: List[str]) -> List[str]:
        check = list(A[0])
        for word in A:
            newCheck = []
            for c in word:
                if c in check:
                    newCheck.append(c)
                    check.remove(c)
            check = newCheck
        
        return check