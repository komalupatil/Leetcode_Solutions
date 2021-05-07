#Leetcode 1441. Build an Array With Stack Operations

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        targetIndex = 0
        
        for i in range(1, target[-1]+1):
            if target[targetIndex] == i:
                result.append("Push")
                targetIndex += 1
            else:
                result.append("Push")
                result.append("Pop")
                
        return result