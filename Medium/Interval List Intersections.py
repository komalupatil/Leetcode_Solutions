#Leetcode 986. Interval List Intersections

class Solution1:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]: 
        a = 0
        b = 0
        intervals = []
        while a < len(A) and b < len(B):
            interval_starting, interval_ending = max(A[a][0], B[b][0]), min(A[a][1], B[b][1])
            
            if interval_starting <= interval_ending:
                intervals.append([interval_starting, interval_ending])
            
            if A[a][1] < B[b][1]:
                a+=1
            else:
                b+=1    
        return intervals

class Solution2:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i,j = 0,0
        result = []
        
        while i< len(A) and j<len(B):
            a_overlaps_b = A[i][0] <= B[j][0] and B[j][0] <= A[i][1]
            b_overlaps_a = B[j][0] <= A[i][0] and A[i][0] <= B[j][1]
            
            if (a_overlaps_b or b_overlaps_a):
                result.append([max(A[i][0], B[j][0]), min(A[i][1], B[j][1])])
                
            if A[i][1] < B[j][1]:
                i+=1
            else:
                j+=1  
        return result
                