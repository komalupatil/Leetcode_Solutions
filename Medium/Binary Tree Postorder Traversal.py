#Leetcode 145. Binary Tree Postorder Traversal

#Solution - Recursive 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.helper(root, res)
        return res
    
    def helper(self, node, result):
        if node:
            self.helper(node.left, result)
            self.helper(node.right, result)
            result.append(node.val)

#Solution - Iterative

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        
        stack = [root]
        
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
                
                
        return res[::-1]