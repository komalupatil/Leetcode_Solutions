#Leetcode 230. Kth Smallest Element in a BST

#use inorder since it gives sorted result
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        res = []
        def in_order(root):
            if root== None:
                return res
            if root:
                if root.left: in_order(root.left)
                res.append(root.val)
                if root.right: in_order(root.right)
            
        in_order(root)
        return res[k-1]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k=k
        self.res= None
        self.helper(root)
        return self.res
        
    def helper(self, root):
        if root == None:
            return
        self.helper(root.left)
        self.k -= 1
        if self.k == 0:
            self.res=root.val
            return
        self.helper(root.right)