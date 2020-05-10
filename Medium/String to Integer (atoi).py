#Leetcode 8. String to Integer (atoi)

#Solution

class Solution:
    def myAtoi(self, str: str) -> int:
        if len(str) == 0:
            return 0
        #remove whitespcaes
        ls = list(str.strip())
        if len(ls) == 0:
            return 0
        sign =1
        #check the first char of the string
        if ls[0] == "-":
            sign = -1
        elif ls[0] == "+":
            sign = 1
        if ls[0]in "-+":del ls[0]
        res, i = 0,0
        while i<len(ls) and ls[i].isdigit():
            res = res*10 + ord(ls[i])-ord("0")
            i+=1
        return max(-2147483648, min(sign*res, 2147483647))