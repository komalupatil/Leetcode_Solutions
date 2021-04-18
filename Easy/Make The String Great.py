#Leetcode 1544. Make The String Great


#Solution
class Solution:
    def makeGood(self, s: str) -> str:
        result = []
        
        for i in s:
            if not result:
                result.append(i)
            elif result[-1].isupper() and result[-1].lower() == i:
                result.pop()
            elif result[-1].islower() and result[-1].upper() == i:
                result.pop()
            else:
                result.append(i)
        
        return "".join(result)