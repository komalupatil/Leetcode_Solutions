#Leetcode 1002. Find Common Characters

#Solution1

from collections import Counter
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        
        counter1 = Counter(A[0])
        
        for a in A[1:]:
            counter2 = Counter(a)
            for k in counter1.keys():
                counter1[k] = min(counter1[k], counter2[k])
        return counter1.elements()



#Solution2

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        
        counter1 = collections.Counter(A[0])
        
        for a in A[1:]:
            counter1 &= Counter(a)
        return list(counter1.elements())