#Leetcode 61. Rotate List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None or k == 0:
            return head
        last = head
        count = 1
        while last.next:
            count +=1
            last = last.next
             
        last.next = head
        curr = head
        
        for _ in range(count - (k % count) -1):
            curr = curr.next
        
        res= curr.next
        curr.next = None
        
        return res