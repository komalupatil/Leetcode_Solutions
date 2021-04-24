#Leetcode 451. Sort Characters By Frequency

#Solution - using bucket sort - similar to Top K frequent elements

class Solution:
    def frequencySort(self, s: str) -> str:
        
        if len(s) == 0:
            return ""
        
        d = {}
        
        for char in s:
            if char in d:
                d[char] +=1
            else:
                d[char] = 1
        
        buckets = [[] for _ in s]
        
        
        for key, value in d.items():
            buckets[value-1].append(key*value) #to print the char by freq doing key*value here
        
        res = ""
        for bucket in buckets[::-1]:
            for char in bucket:
                res += char
        return res


#Solution2

class Solution:
    def frequencySort(self, s: str) -> str:
        if len(s) == 0:
            return ""
        
        d = {}
        
        for char in s:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
                
        s_new = sorted(d, key=lambda x: d[x], reverse=True)
        res = ""
        for char in s_new:
            res += char*d[char]
            
        return res

#SOlution3 - using maxHeap
class Solution:
    def frequencySort(self, s: str) -> str:
        charFreq = {}
        
        for char in s:
            charFreq[char] = charFreq.get(char, 0)+1
        
        maxHeap = []

        for char, freq in charFreq.items():
            heapq.heappush(maxHeap, (-freq, char))
        
        res = ""
        
        while maxHeap:
            freq, char = heapq.heappop(maxHeap)
            for _ in range(-freq):
                res += char
        return res