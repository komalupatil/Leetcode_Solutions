#Leetcode 752. Open the Lock

import collections 
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadSet = set(deadends)
        
        if "0000" in deadSet:
            return -1
        
        seen = set()
        ans = 0
        queue = collections.deque(["0000"])
        seen.add("0000")
        
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                
                if cur == target:
                    return ans
                
                for i in range(4):
                    newDigit1 = (int(cur[i]) + 1) %10
                    newCode1 = cur[:i] + str(newDigit1) + cur[i+1:]
                    
                    if newCode1 not in seen and newCode1 not in deadSet:
                        queue.append(newCode1)
                        seen.add(newCode1)
                    
                    newDigit2 = (int(cur[i]) +10 - 1) %10
                    newCode2 = cur[:i] + str(newDigit2) + cur[i+1:]
                    
                    if newCode2 not in seen and newCode2 not in deadSet:
                        queue.append(newCode2)
                        seen.add(newCode2)
            
            ans += 1
        
        return -1