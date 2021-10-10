#Leetcode 275. H-Index II

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = 0
        r = len(citations)-1
        n = len(citations)
        while l <= r:
            m = l+(r-l)//2
            if citations[m] == n-m: return citations[m]
            if n-m > citations[m]:
                #more papers than citations
                l = m+1
            else:
                #less papers than citations
                r = m-1
            
        return n-l