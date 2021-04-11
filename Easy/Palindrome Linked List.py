#Leetcode 234. Palindrome Linked List

#Topic: Two Pointers, combine reverse and middle of linked list

#Solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        fast = slow = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True