#Leetcode 1417. Reformat The String

class Solution:
    def reformat(self, s: str) -> str:
        result = ""
        digits = []
        alpha = []
        for i in s:
            if i.isdigit():
                digits.append(i)
            else:
                alpha.append(i)
        if abs(len(alpha)-len(digits))<2:
            while digits and alpha:
                result += alpha.pop()
                result += digits.pop()
            if digits:
                result = digits[-1] + result
            elif alpha:
                result = result + alpha[-1]
        return result