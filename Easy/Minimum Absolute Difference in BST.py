#Leetcode 530. Minimum Absolute Difference in BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        l = []
        
        def dfs(node):
            if node:
                if node.left: dfs(node.left)
                l.append(node.val)
                if node.right: dfs(node.right)
        dfs(root)
        minDiff = float('inf')
        for i in range(1,len(l)):
            diff = l[i] - l[i-1]
            if diff < minDiff:
                minDiff = diff
        return minDiff