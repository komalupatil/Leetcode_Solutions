#Leetcode 235. Lowest Common Ancestor of a Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if root == None or not p or not q:
            return None
        
        if (p.val < root.val and q.val < root.val):
            return self.lowestCommonAncestor(root.left, p,q)
        elif (p.val > root.val and q.val > root.val):
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root