#Leetcode 853. Car Fleet

class Solution1:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for pos, s in sorted(zip(position, speed))[::-1]:
            print(pos,s)
            dist = target - pos
            if not stack:
                stack.append(dist / s)
            elif dist / s > stack[-1]:
                stack.append(dist / s)
            print(stack)
        return len(stack)

class Solution2:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        timeToTarget = [float(target-pos)/s for pos, s in sorted(zip(position,speed))]
        result = 0
        current = 0
        
        for time in timeToTarget[::-1]:
            if time > current:
                result +=1 
                current = time
        return result