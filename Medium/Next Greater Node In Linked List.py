#Leetcode 1019. Next Greater Node In Linked List

#Monotonic stack
# build a decreasing stack while finding next greater/larger element
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        arr = []
        temp = head
        while temp:
            arr.append(temp.val)
            temp = temp.next
        
        firstLargerToRight = [0] * len(arr)
        stack = []
        for i in range(len(arr)):
            while len(stack)!= 0 and arr[stack[-1]] < arr[i]:
                firstLargerToRight[stack.pop()] = arr[i]
            
            stack.append(i)
            
        return firstLargerToRight