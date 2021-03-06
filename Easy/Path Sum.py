#Leetcode 112. Path Sum

#Given a binary tree and a sum, determine if the tree has a root-to-leaf path 
#such that adding up all the values along the path equals the given sum.

#Note: A leaf is a node with no children.


#Solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return None
        
        sum -= root.val
        if root.left == None and root.right == None:
            return sum == 0
        
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
        