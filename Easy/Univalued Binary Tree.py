#Leetcode 965. Univalued Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        result = []
        
        def dfs(node):
            if node:
                result.append(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return len(set(result)) == 1