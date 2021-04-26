#Leetcode 744. Find Smallest Letter Greater Than Target

#Solution - binary search
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = 0
        h = len(letters) -1
        ans = 0
        
        while l<=h:
            mid = l+(h-l)//2
            if letters[mid] > target:
                ans = mid
                h = mid -1
            else:
                l = mid + 1
        return letters[ans]