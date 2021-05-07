#Leetcode 696. Count Binary Substrings

class Solution1:
    def countBinarySubstrings(self, s: str) -> int:
        res = 0
        cur = 1
        prev = 0
        
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cur += 1
            else:
                res += min(cur, prev)
                prev = cur
                cur = 1
        return res + min(cur, prev)


class Solution2:
    def countBinarySubstrings(self, s: str) -> int:
        groups = [1]
        
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                groups.append(1)
            else:
                groups[-1] +=1
        ans = 0
        for i in range(1, len(groups)):
            ans += min(groups[i-1], groups[i])
        
        return ans