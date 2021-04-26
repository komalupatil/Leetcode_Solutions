#Leetcode 1470. Shuffle the Array

#Solution
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        p1 = 0
        p2 = n
        
        while p1 < p2 and p2 < 2*n:
            result.append(nums[p1])
            result.append(nums[p2])
            p1+=1
            p2+=1
        return result