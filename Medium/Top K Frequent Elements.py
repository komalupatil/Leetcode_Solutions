#Leetcode 347. Top K Frequent Elements

class Solution1:
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


class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        heap = []
        for key in hashmap:
            heapq.heappush(heap, (-hashmap[key], key))
            
        res = []
        for _ in range(k):
            popped = heapq.heappop(heap)
            res.append(popped[1])
        return res


class Solution3:
        def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            hashmap = {}
            for num in nums:
                if num in hashmap:
                    hashmap[num] += 1
                else:
                    hashmap[num] = 1
            heap = []
            for num, freq in hashmap.items():
                heapq.heappush(heap, (freq, num))
                if len(heap) > k:
                    heapq.heappop(heap)
            
            result = []
            while heap:
                result.append(heapq.heappop(heap)[1])
            
            return result