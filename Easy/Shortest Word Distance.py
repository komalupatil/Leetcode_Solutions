#Leetcode 243. Shortest Word Distance

#Solution

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        ans = float('inf')
        i1 = -1
        i2 = -1
        
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                i1 = i
                
            if wordsDict[i] == word2:
                i2 = i
                
            if i1!=-1 and i2!=-1:
                ans = min(ans, abs(i1-i2))
        return ans
        