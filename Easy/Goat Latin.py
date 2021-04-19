#Leetcode 824. Goat Latin

#Solution
class Solution:
    def toGoatLatin(self, S: str) -> str:
        S = S.split()

        result = []
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        for i, word in enumerate(S):
            if word[0] in vowels:
                word = word + 'ma'
            if word[0] not in vowels:
                word = word[1:] + word[0] + 'ma'
            result.append(word + ('a'*(i+1)))
            
        return " ".join(result)