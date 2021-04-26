#Leetcode 525. Contiguous Array

#Solution using hashmap(dict)
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        maxLength = 0
        table = {0:0}
        
        for index, num in enumerate(nums, 1):
            if num == 0:
                count -=1
            else:
                count +=1
            if count in table:
                maxLength = max(maxLength, index - table[count])
            else:
                table[count] = index
        return maxLength
        