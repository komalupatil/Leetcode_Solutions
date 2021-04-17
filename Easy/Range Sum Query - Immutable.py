#Leetcode 303. Range Sum Query - Immutable

#Solution
class NumArray():
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        for i in range(1, len(nums)):
            self.nums[i] += self.nums[i-1]
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.nums[j] - (self.nums[i-1] if i > 0 else 0)
       # result = 0
        # for num in range(i, j+1):
            #result += self.nums[num]
        #return result


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

#Solution - Prefix Sum

class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum = [0 for _ in range(len(nums)+1)]
                          
        for i in range(1,len(self.prefixSum)):
            self.prefixSum[i] = self.prefixSum[i-1] + nums[i-1]
            
    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum[right+1] - self.prefixSum[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)