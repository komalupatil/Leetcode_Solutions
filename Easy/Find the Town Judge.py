#Leetcode 997. Find the Town Judge

#Solution

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