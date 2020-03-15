#leetcode 1313. Decompress Run-Length Encoded List

#solution1 

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0, len(nums), 2):
            result.extend(nums[i]*[nums[i+1]])
        return result



#solution2

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        return sum([nums[i]*[nums[i+1]] for i in range(0,len(nums),2)],[])
            
