#Leetcode 1688. Count of Matches in Tournament

class Solution1:
    def numberOfMatches(self, n: int) -> int:
        
        res = 0
        
        while (n != 1):
            if n%2 == 0:
                res += n//2
                n = n//2
                
            else:
                res += (n-1)//2
                n = (n-1)//2+1     
        return res


class Solution2:
    def numberOfMatches(self, n: int) -> int:
        return n-1
