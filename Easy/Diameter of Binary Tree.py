#Leetcode 543. Diameter of Binary Tree

#First do maxDepth for understanding the diameter of binary tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        self.max = 0
        
        def depth(node):
            
            if node == None:
                return 0
            
            left = depth(node.left)
            right = depth(node.right)
            self.max = max(self.max, left + right)
            
            return 1 + max(left, right)
        
        depth(root)
        return self.max124. Binary Tree Maximum Path Sum