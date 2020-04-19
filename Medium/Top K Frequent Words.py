#Leetcode 692. Top K Frequent Words

#Solution - using bucket sort - similar to top k frequent elements

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]: 
        if len(words) == 0:
            return []
        if len(words) == 1:
            return words
        
        d={}
        
        for word in words:
            if word in d:
                d[word] +=1
            else:
                d[word] =1
        
                
        buckets = [[] for _ in range(len(words))]
        
        for key, val in d.items():
            buckets[val-1].append(key)
        
        
        res = []
        
        for bucket in buckets[::-1]:
            bucket.sort()
            for word in bucket:
                if len(bucket) == 0:
                    continue
                if len(res) == k:
                    return res
                else:
                    res.append(word)
        return res
            
            
        