#leetcode 3
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        ws = 0
        maxLength = 0
        for i in range(len(s)):
            if s[i] in d and ws <= d[s[i]]:
                ws = d[s[i]] + 1
            else:
                maxLength = max(maxLength, i - ws + 1)
            d[s[i]] = i
        return maxLength
