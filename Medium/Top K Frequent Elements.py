#Leetcode 347. Top K Frequent Elements


#Solution - using hash map and bucket sort


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <k:
            return nums
        if len(nums) == 0:
            return 0
        
        d = {}
        
        for num in nums:
            if num in d:
                d[num] +=1
            else:
                d[num] =1
                
        buckets = [[] for _ in range(len(nums))]
        
        for key, val in d.items():
            buckets[val-1].append(key)
        
        
        res=[]
        for bucket in buckets[::-1]:
            for num in bucket:
                if len(res) == k:
                    return res
                res.append(num)
        return res

