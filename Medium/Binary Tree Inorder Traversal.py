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


#Solution2 - Iterative 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], []
        
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmp = stack.pop()
                res.append(tmp.val)
                root = tmp.right
        return res