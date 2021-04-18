#Leetcode 997. Find the Town Judge

#Solution1
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if trust == [] and N==1:
            return 1
        count = [0] * (N+1)
        for i,j in trust:
            # Keep track of the cumulative score of each person: 
            # if person a trusts person b, 
            # we decrement a's score and increment b's score.
            count[i] -=1
            count[j] +=1
        print(count)
        for i in range(1,N+1):
            #The judge is the only person that ends up with a score of N-1
            if count[i] == N-1:
                return i
        return -1

#Solution2
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if len(trust) < N - 1:
            return -1
    
        indegree = [0] * (N + 1)
        outdegree = [0] * (N + 1)
    
        for a, b in trust:
            outdegree[a] += 1
            indegree[b] += 1
        
        for i in range(1, N + 1):
            if indegree[i] == N - 1 and outdegree[i] == 0:
                return i
        return -1