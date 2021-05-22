#Leetcode 22. Generate Parentheses

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        self.generateParans(n, n, "", result)
        
        return result
    
    def generateParans(self, leftNeededParans, rightNeededParans, stringInProgress, result):
        if leftNeededParans == 0 and rightNeededParans == 0:
            result.append(stringInProgress)
        
        if leftNeededParans >0:
            self.generateParans(leftNeededParans-1, rightNeededParans, stringInProgress + "(", result)
        if leftNeededParans < rightNeededParans:
            self.generateParans(leftNeededParans, rightNeededParans-1, stringInProgress + ")", result)