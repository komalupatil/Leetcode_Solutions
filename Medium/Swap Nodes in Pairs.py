#Leetcode 24. Swap Nodes in Pairs

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while head is not None and head.next is not None:
            firstNode = head
            secondNode = head.next
            
            prev.next = secondNode
            firstNode.next = secondNode.next
            secondNode.next = firstNode
            
            prev = firstNode
            head = firstNode.next
        
        return dummy.next