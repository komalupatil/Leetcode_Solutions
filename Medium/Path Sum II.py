#Leetcode 113. Path Sum II

#Given a binary tree and a sum, find all root-to-leaf paths 
#where each path's sum equals the given sum.
#Note: A leaf is a node with no children.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        res = []
        self.dfs(root, targetSum, [], res)
        return res
        
    def dfs(self, root, targetSum, ls, res):
        if root:
            if not root.left and not root.right and targetSum == root.val:
                ls.append(root.val)
                res.append(ls)
            self.dfs(root.left, targetSum-root.val, ls+[root.val], res)
            self.dfs(root.right, targetSum-root.val, ls+[root.val], res)
        