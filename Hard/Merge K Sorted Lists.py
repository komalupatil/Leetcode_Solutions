#leetcode23
#Solution1
#merge k sorted lists using heapq (not optimal) as we are interating through all the lists and putting them in heap
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        h = []
        for node in lists:
            while node:
                heapq.heappush(h, node.val)
                node = node.next
        head = dummy = ListNode(0)
        while h:
            val = heapq.heappop(h)
            head.next = ListNode(val)
            head = head.next
        
        return dummy.next


#Solution2
#using priority queue (optimal as we are only storing first elements of each list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    ListNode.__eq__ = lambda self, other: self.val == other.val
    ListNode.__lt__ = lambda self, other: self.val < other.val
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        from queue import PriorityQueue
        head = dummy = ListNode(None)
        pq = PriorityQueue()
        for _list in lists:
            if _list:
                pq.put((_list.val, _list))
        
                
        while not pq.empty():
            val, node = pq.get()
            dummy.next = ListNode(val)
            dummy = dummy.next
            node = node.next
            if node:
                pq.put((node.val, node))
  
        return head.next

