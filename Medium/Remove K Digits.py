#Leetcode 402. Remove K Digits

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for i in range(len(num)):
            while k > 0 and len(stack) > 0 and stack[-1] > num[i]:
                stack.pop()
                k -= 1
            stack.append(num[i])
            
        while k>0:
            stack.pop()
            k -= 1
        
        ans = ""
        for i in range(len(stack)):
            ans += stack[i]
        
        d = 0
        while d < len(ans) and ans[d] == "0":
            d += 1
                
        res = ""
        while d < len(ans):
            res += ans[d]
            d += 1
        
        if len(res) == 0:
            return "0"
        return res