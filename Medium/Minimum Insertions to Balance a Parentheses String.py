#Leetcode 1541. Minimum Insertions to Balance a Parentheses String

class Solution:
    def minInsertions(self, s: str) -> int:
        if s == None or len(s) == 0:
            return 0
        
        pair = 0
        count = 0
        
        s= s.replace("))", "}")
        
        for i in s:
            if i == "(":
                pair += 1
            elif pair > 0 and (i == ")" or i == "}"):
                
                pair -= 1
                #single ) bracket means we need something extra
                if i == ")":
                    count += 1
            else:
                #without ( bracket -- we have either } or )
                if i == ")":
                    count += 2
                else:
                    count += 1
        return pair*2 + count