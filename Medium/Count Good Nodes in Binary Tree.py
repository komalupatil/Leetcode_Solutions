#Leetcode 1448. Count Good Nodes in Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        count = [0]
        self.dfs(root, root.val, count)
        
        return count[0]
    
    def dfs(self, root, maxSoFar, count):
        if root.val >= maxSoFar:
            count[0] += 1
        
        if root.left is not None:
            self.dfs(root.left, max(root.left.val, maxSoFar), count)
        
        if root.right is not None:
            self.dfs(root.right, max(root.right.val, maxSoFar), count)