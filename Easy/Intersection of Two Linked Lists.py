#Leetcode 160. Intersection of Two Linked Lists

#Solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pA = headA
        pB = headB
        
        while pA is not pB:
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next
        return pA