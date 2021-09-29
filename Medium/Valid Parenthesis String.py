#Leetcode 678. Valid Parenthesis String

class Solution1:
    def checkValidString(self, s: str) -> bool:
        if len(s) == 0 or s== "*":
            return True
        if s == "(" or s == ")":
            return False
        left_count = 0
        for i in s:
            if i == ")":
                left_count -= 1
            else:
                left_count +=1
            if left_count < 0:
                return False
        if left_count == 0:
            return True
        
        right_count = 0
        for i in reversed(s):
            if i == "(":
                right_count -= 1
            else:
                right_count +=1
            if right_count < 0:
                return False
        return True


class Solution2:
    def checkValidString(self, s: str) -> bool:
        if len(s) == 0:
            return True
        left_count = 0
        right_count = 0
        for i in range(len(s)):
            left_count +=1 if s[i] in "(*" else -1
            right_count +=1 if s[len(s)-i-1] in ")*" else -1
            if left_count < 0 or right_count < 0:
                return False
    
        return True


class Solution3:
    def checkValidString(self, s: str) -> bool:
        class Solution:
    def checkValidString(self, s: str) -> bool:
        if len(s) == 0:
            return True
        
        opn = []
        star = []
        
        for i in range(len(s)):
            if s[i] == "(":
                opn.append(i)
            elif s[i] == "*":
                star.append(i)
            else:
                if len(opn) != 0:
                    opn.pop()
                elif len(star) != 0:
                    star.pop()
                else:
                    return False
                
        while opn:
            if len(star) == 0:
                return False
            elif opn[-1] < star[-1]:
                opn.pop()
                star.pop()
            else:
                return False
        return True