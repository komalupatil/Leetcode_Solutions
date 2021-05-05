#Leetcode 1051. Height Checker

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        new_h = sorted(heights)
        res = 0
        for i in range(len(heights)):
            if heights[i] != new_h[i]:
                res += 1
        return res