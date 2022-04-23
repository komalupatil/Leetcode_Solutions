#Leetcode 65. Valid Number

class Solution:
    def isNumber(self, s: str) -> bool:
        if len(s) == None:
            return False
        
        exponentSeen = False
        digitSeen = False
        dotSeen = False
        
        
        for i in range(len(s)):
            if s[i].isdigit():
                digitSeen = True
            elif s[i] == '+' or s[i] == '-':
                if (i>0 and s[i-1] != 'e' and s[i-1] != 'E'):
                    return False
            elif s[i] == 'e' or s[i] == 'E':
                if exponentSeen or not digitSeen:
                    return False
                digitSeen = False
                exponentSeen = True
            elif s[i] == '.':
                if dotSeen or exponentSeen:
                    return False
                dotSeen = True
            else:
                return False
        return digitSeen 