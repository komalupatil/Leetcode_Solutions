#Leetcode 112. Path Sum

#Given a binary tree and a sum, determine if the tree has a root-to-leaf path 
#such that adding up all the values along the path equals the given sum.
#Note: A leaf is a node with no children.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return None
        
        sum -= root.val
        if root.left == None and root.right == None:
            return sum == 0
        
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root is None:
            return False
        
        if root.val == targetSum and root.left == None and root.right == None:
            return True
        
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum-root.val)
        