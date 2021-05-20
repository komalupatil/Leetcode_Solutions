#Leetcode 91. Decode Ways

class Solution1:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        dp = [0 for _ in range(len(s)+1)]
        
        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1
        
        for i in range(2, len(s)+1):
            if 0< int(s[i-1:i]) <=9:
                dp[i] += dp[i-1]
            if 10<= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
            
        return dp[len(s)]

class Solution2:
    def numDecodings(self, s: str) -> int:
        mapping = set([str(x) for x in range(1, 27)])
        
        if len(s) == 1:
            return int(s[0] in mapping)
        
        T = [0]*len(s)
        T[0] = int(s[0] in mapping)
        T[1] = (s[0] in mapping and s[1] in mapping) + (s[:2] in mapping)

        for i in range(2,len(s)):
            T[i] = (s[i] in mapping) * T[i-1] + (s[i-1:i+1] in mapping)* T[i-2]
        
        return T[-1]
        