#Leetcode 139. Word Break

#Solution - dp
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[0] = True
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i] and s[i:j+1] in wordDict:
                    print(s[i:j+1])
                    dp[j+1] = True
        return dp[-1]