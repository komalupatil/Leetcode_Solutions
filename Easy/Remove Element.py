#Leetcode 27. Remove Element

#Starting from the left every time we find a value that is the target value we swap it out with an item starting from the right. 
#We decrement end each time as we know that the final item is the target value and only increment start once we know the value is ok. 
#Once start reaches end we know all items after that point are the target value so we can stop there.

class Solution1:
    def removeElement(self, nums: List[int], val: int) -> int:
        start = 0
        end = len(nums)-1
        while start <= end:
            if nums[start] == val:
                nums[start], nums[end], end = nums[end], nums[start], end-1
            else:
                start +=1
        return start

class Solution2:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0  
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i+=1
        return i