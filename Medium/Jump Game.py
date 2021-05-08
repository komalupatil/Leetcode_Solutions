#Leetcode 55. Jump Game

#jump taken must be atleast equal to the index
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachjump = 0
        
        for i in range(len(nums)):
            if i > reachjump:
                return False
            reachjump = max(reachjump, i + nums[i])
        return True