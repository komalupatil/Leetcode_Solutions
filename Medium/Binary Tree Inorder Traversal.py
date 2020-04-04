#Leetcode 94. Binary Tree Inorder Traversal

#Solution1 - recursive

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        self.inorder(root, output)
        return output
    def inorder(self, root, output):
        if root:
            
            self.inorder(root.left, output)
            output.append(root.val)
            self.inorder(root.right, output)