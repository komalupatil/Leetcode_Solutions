# Leetcode 1119. Remove Vowels from a String

#Solution
class Solution(object):
    def removeVowels(self, S):
        newS = ""
        vowel_set = {'a', 'e', 'i', 'o', 'u'}
        for i in S:
            if i not in vowel_set:
                newS += i
        return newS

solution = Solution()
string = solution.removeVowels("leetcodeisacommunityforcoders")
print(string)
            
