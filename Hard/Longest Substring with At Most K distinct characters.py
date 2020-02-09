#leetcode340 - Longest Substring with At Most K Distinct Characters
#time O(n), space O(1)
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        maxLength = 0
        char_freq = {}
        winStart = 0
        for winEnd in range(len(s)):
            right_char = s[winEnd]
            if right_char not in char_freq:
                char_freq[right_char] = 0
            char_freq[right_char] +=1
            while len(char_freq) > k:
                left_char = s[winStart]
                char_freq[left] -= 1
                if char_freq[left] == 0:
                    del char_freq[left]
                winStart +=1
        maxLength = max(maxLength, (winEnd-winStart+1))

        return maxLength                
