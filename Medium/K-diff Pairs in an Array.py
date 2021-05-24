#Leetcode 532. K-diff Pairs in an Array

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        hashmap = {}
        result = set()
        #{3:0, 1:1, 4:2, 1:3, 5:4}
        #[3,1,4,1,5]
        
        for i, num in enumerate(nums):
            hashmap[num] = i
            
        for j,num in enumerate(nums):
            if num-k in hashmap and (num, num-k) not in result and hashmap[num-k] != j:
                result.add((num,num-k))
        return len(result)