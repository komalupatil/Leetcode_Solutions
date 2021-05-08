#Leetcode 345. Reverse Vowels of a String

class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        l = 0
        r = len(s)-1
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        while l<r:
            if s[l] in vowels and s[r] in vowels:
                tmp = s[l]
                s[l] = s[r]
                s[r] = tmp
                l+=1
                r-=1
            if s[l] not in vowels:
                l+=1
            if s[r] not in vowels:
                r-=1
        return "".join(s)