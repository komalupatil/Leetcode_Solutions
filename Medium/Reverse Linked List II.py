#Leetcode 92. Reverse Linked List II

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m==n:
            return head
        
        i=0
        current, prev = head, None
        while current is not None and i<m-1:
            prev = current
            current = current.next
            i+=1
        
        last_node_of_first_part = prev
        last_node_of_sub_subList = current
        
        i = 0
        next1  = None
        while current is not None and i<n-m+1:
            next1 = current.next
            current.next = prev
            prev = current
            current = next1
            i+=1
        
        if last_node_of_first_part is not None:
            last_node_of_first_part.next = prev
        else:
            head = prev
            
        last_node_of_sub_subList.next = current
        
        return head