#Leetcode 1353. Maximum Number of Events That Can Be Attended

#Grredy Approach
#Refer; https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/discuss/1116371/Python-With-detailed-explanation
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        total_days = max(end for start, end in events)
        event_id = 0
        no_of_events_attended = 0
        min_heap = []
        
        for day in range(1, total_days+1):
            ## Adding all the events that are starting today
            while event_id < len(events) and events[event_id][0] == day:
                heappush(min_heap, events[event_id][1])
                event_id += 1
            
            # Remove all the events whose end date was before today
            while min_heap and min_heap[0] < day:
                heappop(min_heap)
            
             # if there is any event that can be attended today, attend it and increment no. of events
            if min_heap:
                heappop(min_heap)
                no_of_events_attended += 1
        
        return no_of_events_attended