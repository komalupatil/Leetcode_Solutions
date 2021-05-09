#Leetcode 139. Word Break

class Solution1:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[0] = True
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i] and s[i:j+1] in wordDict:
                    print(s[i:j+1])
                    dp[j+1] = True
        return dp[-1]

class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        q = deque([s])
        seen = set() 
        while q:
            s = q.popleft() 
            for word in wordDict:
                if s.startswith(word):
                    new_s = s[len(word):]
                    if new_s == "": 
                        return True
                    if new_s not in seen:
                        q.append(new_s)
                        seen.add(new_s)
        return False
            