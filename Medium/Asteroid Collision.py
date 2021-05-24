#Leetcode 735. Asteroid Collision

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        i = 0
        while i < len(asteroids):
            if asteroids[i] > 0:
                stack.append(asteroids[i])
            else:
                while (stack and stack[-1] > 0 and stack[-1] < abs(asteroids[i])):
                       stack.pop()
                if (not stack or stack[-1] < 0):
                       stack.append(asteroids[i])
                elif stack[-1] == abs(asteroids[i]):
                       stack.pop()
            i +=1
            
        
        return stack