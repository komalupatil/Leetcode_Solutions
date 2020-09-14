#Leetcode 206. Reverse Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        
        previous = None
        current = head
        next = head
        
        while (current != None):
            next = current.next
            current.next = previous #reverse operation
            previous = current
            current = next
        return previous