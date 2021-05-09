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
        stack1 = []
        stack2 = []
        for index, value in enumerate(s):
            if value == "(":
                stack1.append(index)
            elif value == "*":
                stack2.append(index)
            else:
                if len(stack1) >0:
                    stack1.pop()
                elif len(stack2) > 0:
                    stack2.pop()
                else:
                    return False
        while stack1 and stack2:
            if stack1[-1] < stack2[-1]:
                stack1.pop()
                stack2.pop()
            else:
                break
        return len(stack1) == 0