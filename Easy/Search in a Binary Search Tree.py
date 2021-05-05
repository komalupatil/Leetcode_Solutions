#Leetcode 700. Search in a Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        currentNode = root
        while currentNode != None:
            if currentNode.val == val:
                return currentNode
            elif currentNode.val < val:
                currentNode = currentNode.right
            else:
                currentNode = currentNode.left
        return None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root and root.val == val:
            return root
        if root and root.val < val:
            return self.searchBST(root.right, val)
        if root and root.val > val:
            return self.searchBST(root.left, val)
        return None