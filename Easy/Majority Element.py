#leetcode169 Majority Element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d:
                d[i] +=1
            else:
                d[i] = 1
        for num in d:
            if d[num] > len(nums)/2:
                return num
