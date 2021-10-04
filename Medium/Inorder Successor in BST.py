#Leetcode 285. Inorder Successor in BST

#refer: https://www.youtube.com/watch?v=5cPbNCrdotA&ab_channel=mycodeschool
#https://github.com/rishijd/python-learning/blob/master/data-structures/trees-inorder-successor.py


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        current = self.findNode(root, p)
        
        if current is None:
            return None
        
        if current.right:
            return self.findMin(current.right)
        
        else:
            successor = None
            ancestor = root
            while ancestor != current:
                if current.val < ancestor.val:
                    successor = ancestor
                    ancestor = ancestor.left
                else:
                    ancestor = ancestor.right
                    
        return successor
        

    
    def findNode(self, root, data):
        if root == None:
            return None
        if root.val == data.val:
            return root
        elif root.val > data.val:
            return self.findNode(root.left, data)
        else:
            return self.findNode(root.right, data)
    
    def findMin(self, root):
        if root is None:
            return None
        
        while root.left != None:
            root = root.left
        return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution2:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        successor = None
    
        while root:
            if p.val < root.val:
                successor = root
                root = root.left
            else:
                root = root.right
        
        return successor