#Leetcode 1071. Greatest Common Divisor of Strings

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:
            return ""
        if str1 == str2:
            return str1
        else:
            length_of_gcd = math.gcd(len(str1), len(str2))
            return self.gcdOfStrings(str1[:length_of_gcd], str2[:length_of_gcd])