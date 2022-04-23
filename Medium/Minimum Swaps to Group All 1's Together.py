#Leetcode 1151. Minimum Swaps to Group All 1's Together

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        windowSize = 0
        
        for i in range(len(data)):
            windowSize += data[i]
        
        curOnesInWindow = 0
        MaxOnesInWindow = 0

        
        for i in range(len(data)):
            curOnesInWindow += data[i]
            if i >= windowSize:
                curOnesInWindow -= data[i - windowSize]
            
            MaxOnesInWindow = max(MaxOnesInWindow, curOnesInWindow)
        
        return windowSize - MaxOnesInWindow