#Leetcode 243. Shortest Word Distance

class Solution:
    def shortestDistance(self, wordsDict, word1, word2):
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

obj = Solution()
words = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "coding"
word2 = "practice"
print(obj.shortestDistance(words, word1, word2))
word3 = "makes"
word4 = "coding"
print(obj.shortestDistance(words, word3, word4)) 
   