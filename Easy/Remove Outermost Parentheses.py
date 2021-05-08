#Leetcode 1021. Remove Outermost Parentheses

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        result = []
        balance = 0
        i = 0
        for j in range(len(S)):
            if S[j] == "(":
                balance +=1
            elif S[j] == ")":
                balance -=1
            if balance == 0:
                    result.append(S[i+1:j])
                    i = j+1
        return "".join(result)