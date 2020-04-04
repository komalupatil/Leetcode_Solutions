#Leetcode 145. Binary Tree Postorder Traversal

#Solution1 - Recursive

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        self.postorder(root, output)
        return output
    def postorder(self, root, output):
        if root:
            self.postorder(root.left, output)
            self.postorder(root.right, output)
            output.append(root.val)