#Leetcode 274. H-Index

# O(n logn) + O(n)
class Solution1:
    def hIndex(self, citations: List[int]) -> int:
        # 6,5,3,1,0
        # 1,2,3,4,5
        
        citations.sort(reverse = True)
        n = len(citations)
        i = 1
        
        while i <= n:
            if citations[i-1] < i:
                break
            i = i+1
        return i-1

#o(n)
class Solution2:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        papers = [0] * (n + 1)  # papers[i] is the number of papers with i citations.
        for c in citations:
            papers[min(n, c)] += 1  # All papers with citations larger than n is count as n.
        i = n
        s = papers[n]  # sum of papers with citations >= i
        while i > s:
            i -= 1
            s += papers[i]
        return i

        
#o(nlogn)+o(logn)
class Solution3:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
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
            