#Leetcode 104. Maximum Depth of Binary Tree

#Solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        return 1 + max(left, right)