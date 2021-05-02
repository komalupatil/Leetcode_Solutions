#Leetcode 821. Shortest Distance to a Character

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        charIndex = float('-inf')
        ans = []
        
        for i,x in enumerate(s):
            if x == c:
                charIndex = i
            ans.append(i-charIndex)
        
        charIndex = float('inf')
        for i in range(len(s)-1, -1, -1):
            if s[i] == c:
                charIndex = i
            ans[i] = min(ans[i], charIndex-i)
        
        return ans