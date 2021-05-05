#Leetcode 1460. Make Two Arrays Equal by Reversing Sub-arrays

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        counter = collections.defaultdict(int)
        
        for t in target:
            counter[t] += 1
        
        for a in arr:
            if a not in counter or counter[a] == 0:
                return False
            counter[a] -= 1
        return all(v==0 for v in counter.values())