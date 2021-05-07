#Leetcode 1290. Convert Binary Number in a Linked List to Integer

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution1:
    def getDecimalValue(self, head: ListNode) -> int:
        result = []
        temp = head
        while temp:
            result.append(temp.val)
            temp = temp.next
        ans = 0
        for i in result:
            ans = 2*ans + i
        
        return ans

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution2:
    def getDecimalValue(self, head: ListNode) -> int:
        ans = 0
        while head:
            ans = 2*ans + head.val
            head = head.next
        return ans