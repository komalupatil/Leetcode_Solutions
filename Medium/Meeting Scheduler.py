#Leetcode 1229. Meeting Scheduler

#based on leetcode 986 interval list intersections
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        i,j= 0,0
        
        slots1.sort(key=lambda x:x[0])
        slots2.sort(key=lambda x:x[0])
        
        while(i< len(slots1) and j < len(slots2)):
            slot1_overlaps_slot2 = slots1[i][0] <= slots2[j][0] and slots2[j][0] <= slots1[i][1]
            slot2_overlaps_slot1 = slots2[j][0] <= slots1[i][0] and slots1[i][0] <= slots2[j][1]
            
            if slot1_overlaps_slot2 or slot2_overlaps_slot1:
                a = max(slots1[i][0], slots2[j][0])
                b = min(slots1[i][1], slots2[j][1])
                if b -a >= duration:
                    return [a,a+duration]
            if slots1[i][1] < slots2[j][1]:
                i+=1
            else:
                j+=1
            
        return []


