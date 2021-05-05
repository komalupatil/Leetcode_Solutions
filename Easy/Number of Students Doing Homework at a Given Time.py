#Leetcode 1450. Number of Students Doing Homework at a Given Time

class Solution1:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        p1 = 0
        p2 = 0
        
        res = 0
        
        while p1<len(startTime) and p2<len(endTime):
            if startTime[p1] <= queryTime <= endTime[p2]:
                res += 1
                p1 += 1
                p2 += 1
            else:
                p1 += 1 
                p2 += 1
            
        return res 

class Solution2:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        res = 0
        for s,e in zip(startTime, endTime):
            if s<=queryTime<= e:
                res +=1
        return res