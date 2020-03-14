#leetcode 1365. How Many Numbers Are Smaller Than the Current Number

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        index = {}
        for i, num in enumerate(sorted(nums)):
            index.setdefault(num, i)
        return [index[num] for num in nums]
