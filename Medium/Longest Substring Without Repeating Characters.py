#leetcode 3
#using sliding window pattern

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        WS = 0
        maxLength = 0
        for WE in range(len(s)):
            if s[WE] in d:
                WS = max(WS, d[s[WE]]+1)
                #example "abcdeca", to select the largest start always and when repeated a comes it should not again start from first a, instead it should start from first "c" occurence +1
            maxLength = max(maxLength, WE - WS + 1)
            d[s[WE]] = WE
        return maxLength
