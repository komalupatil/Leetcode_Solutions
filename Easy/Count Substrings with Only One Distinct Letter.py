#Leetcode 1180. Count Substrings with Only One Distinct Letter

class Solution:
    def countLetters(self, s: str) -> int:
        total = 1
        dp = [0] * len(s)
        dp[0]  = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = 1
            total += dp[i]
        return total