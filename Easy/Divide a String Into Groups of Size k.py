#Leetcode 2138. Divide a String Into Groups of Size k

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        result = []
        for i in range(0, len(s), k):
            result.append(s[i:i+k])
        
        if len(result[-1]) != k:
            while len(result[-1]) < k:
                result[-1] += fill
        
        return result