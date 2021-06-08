#Leetcode 150. Evaluate Reverse Polish Notation

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token == "+" or token == "-" or token == "*" or token == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                if token == "+":
                    result = num2 + num1
                elif token == "-":
                    result = num2 - num1
                elif token == "*":
                    result = num2 * num1
                else:
                    result = num2/num1
                    
                stack.append(int(result))
            else:
                stack.append(int(token))
        return stack.pop()