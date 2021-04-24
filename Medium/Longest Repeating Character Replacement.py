#Leetcode 424. Longest Repeating Character Replacement

#Solution
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength, windowStart, max_repeating_letter_count = 0,0,0
        
        freq = {}
        
        for windowEnd in range(len(s)):
            rightChar = s[windowEnd]
            freq[rightChar] = freq.get(rightChar, 0)+1
            
            max_repeating_letter_count = max(max_repeating_letter_count, freq[rightChar])
            
            if (windowEnd-windowStart+1 - max_repeating_letter_count) > k:  #IMP
                leftChar = s[windowStart]
                freq[leftChar] -= 1
                if freq[leftChar] == 0:
                    del freq[leftChar]
                windowStart += 1
            maxLength = max(maxLength, windowEnd-windowStart+1)
        return maxLength