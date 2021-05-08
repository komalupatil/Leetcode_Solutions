#Leetcode 496. Next Greater Element I

#monotonic stack, next greater so create decreasing stack and keep track of it in hashable
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        d = {}
        stack = []
        ans = []
        
        for i in nums2:
            while len(stack) and stack[-1]<i:
                d[stack.pop()] = i
            stack.append(i)
            
        for i in nums1:
            ans.append(d.get(i, -1))
        return ans