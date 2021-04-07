#Leetcode 389. Find the Difference

#Solution1
class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dicti = {}
        for i in range(len(s)):
            if s[i] in dicti.keys():
                dicti[s[i]] += 1
            else:
                dicti[s[i]] = 1
        for j in range(len(t)):
            if t[j] in dicti.keys():
                dicti[t[j]] -= 1
            else:
                dicti[t[j]] = 1
        for k,v in dicti.items():
            if v != 0:
                return k

#Solution2 - using xor, xor of num with itself is 0 and xor of num with 0 is num.
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans = 0
        for letter in s:
            ans ^= ord(letter)
        for letter in t:
            ans ^= ord(letter)
        return chr(ans)