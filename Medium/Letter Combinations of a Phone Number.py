#Leetcode 17. Letter Combinations of a Phone Number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(mapping[digits[0]])
        
        result = []
        path = ""
        self.dfs(digits, 0, path, mapping, result)
        return result
    
    def dfs(self, digits, index, path, mapping, result):
        if index == len(digits):
            result.append(path)
            return
        string = mapping[digits[index]]
        for c in string:
            self.dfs(digits, index+1, path + c, mapping, result)