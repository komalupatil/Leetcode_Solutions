#Leetcode 1684. Count the Number of Consistent Strings

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            for char in word:
                if char not in allowed:
                    count += 1
                    break
        return len(words) - count