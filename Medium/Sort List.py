#Leetcode 148. Sort List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        
        
        prev = None
        slow = head
        fast = head
        
        while(fast != None and fast.next != None):
            prev = slow
            slow = slow.next
            fast = fast.next.next
            
        prev.next = None
        
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        
        return self.merge(l1, l2)
    
    def merge(self, h1, h2):
        dummy = tail = ListNode(None)
        while h1 and h2:
            if h1.val < h2.val:
                tail.next, h1 = h1, h1.next
            else:
                tail.next, h2 = h2, h2.next
            tail = tail.next
        
        if h1 != None:
            tail.next = h1
        if h2 != None:
            tail.next = h2

        return dummy.next