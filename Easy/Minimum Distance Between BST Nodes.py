#Leetcode 783. Minimum Distance Between BST Nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def minDiffInBST(self, root: TreeNode) -> int:
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

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    pre = -float('inf')
    res = float('inf')
    def minDiffInBST(self, root: TreeNode) -> int:
        if root.left:
            self.minDiffInBST(root.left)
        self.res = min(self.res, root.val - self.pre)
        self.pre = root.val
        if root.right:
            self.minDiffInBST(root.right)
        return self.res