#leetcode 3
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        WS = 0
        maxLength = 0
        for WE in range(len(s)):
            if s[WE] in d:
                WS = max(WS, d[s[WE]]+1)
            maxLength = max(maxLength, WE - WS + 1)
            d[s[WE]] = WE
        return maxLength
