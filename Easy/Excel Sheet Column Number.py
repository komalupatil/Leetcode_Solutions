#leetcode171. Excel Sheet Column Number

class Solution:
    def titleToNumber(self, s: str) -> int:
        
        colNum = 0
        for i in s:
            colNum = colNum *26 + (ord(i)-ord('A')+1)
        return colNum
