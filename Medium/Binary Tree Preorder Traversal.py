#Leetcode 144. Binary Tree Preorder Traversal

#Solution1 recursive:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        self.preorder(root, output)
        return output
        
    def preorder(self, root, output):
        if root: 
            
            output.append(root.val)
            self.preorder(root.left, output)
            self.preorder(root.right, output)