#Leetcode 1598. Crawler Log Folder

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        
        for i in logs:
            if i == "../":
                count = max(0, count-1)
            elif i == "./":
                continue
            else:
                count += 1
        
        if count < 0:
            return 0
        else:
            return count