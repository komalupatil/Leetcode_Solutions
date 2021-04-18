#Leetcode 415. Add Strings


#Solution 
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) == 0:
            return num2
        if len(num2) == 0:
            return num1
        
        result = []
        
        i = len(num1)-1
        j = len(num2)-1
        
        carry = 0
        
        
        #continue till both are strings are empty
        while i>=0 or j>=0:
            addition = 0
            
            #add carry to sum
            addition += carry
            
            if i>= 0:
                #subtract ascii value of 0 from num
                addition += ord(num1[i]) - ord('0')
                i-=1
            
            if j>= 0:
                addition += ord(num2[j]) - ord('0')
                j-=1
                
            carry = addition//10
            result.append(addition %10)
        if carry !=0:
            result.append(carry)
        
        return "".join([str(i) for i in result])[::-1]