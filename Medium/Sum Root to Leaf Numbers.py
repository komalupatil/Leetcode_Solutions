#Leetcode 129. Sum Root to Leaf Numbers


#Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
#An example is the root-to-leaf path 1->2->3 which represents the number 123.
#Find the total sum of all root-to-leaf numbers.
#Note: A leaf is a node with no children.


#Solution


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    finalSum = 0
    def sumNumbers(self, root: TreeNode) -> int:
        self.findSum(root, "")
        return self.finalSum
    
    def findSum(self, root, currentSum):
        if root == None:
            return None
        
        currentSum += str(root.val)
        
        if root.left == None and root.right== None:
            self.finalSum = self.finalSum + int(currentSum)
        
        else:
            self.findSum(root.left, currentSum)
            self.findSum(root.right, currentSum)
             