#Leetcode 682. Baseball Game

#Solution

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        
        result = []
        
        for i in ops:
            if i == "C":
                del result[-1]
            elif i == "D":
                result.append(2*int(result[-1]))
            elif i == "+":
                result.append(int(result[-1])+int(result[-2]))
            else:
                result.append(i)
            print(result)
        
        output = 0
        for res in result:
            output += int(res)
        return output