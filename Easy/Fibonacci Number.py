#Leetcode 509. Fibonacci Number

class Solution1:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
    
        a,b=0,1
        for _ in range(n):
            a,b=b,a+b
        return a

class Solution2:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
    
        return self.fib(n-1) + self.fib(n-2)