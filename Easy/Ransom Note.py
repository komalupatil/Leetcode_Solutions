#Leetcode 383. Ransom Note

#Solution1

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        letters = {}
        for letter in magazine:
            if letter in letters:
                letters[letter] +=1
            else:
                letters[letter] = 1
        for letter in ransomNote:
            if letter in letters:
                letters[letter] -=1
                if letters[letter] == 0:
                    del letters[letter]
            else:
                return False
        return True

#Soltuion2 using set() and count()

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        for i in set(ransomNote):
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True