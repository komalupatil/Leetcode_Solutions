#Leetcode 516. Longest Palindromic Subsequence

#similar to longest common subsequence, in this case, seccond string to compare will be the reverse of given string
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s1 = s
        s2 = s[::-1]
        m = len(s1)
        n = len(s2)
        
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] ==s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]