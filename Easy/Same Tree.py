#Leetcode 100. Same Tree

#Solution - Iterative


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        stack = []
        stack.append((p, q))
        
        while stack:
            
            node1, node2 = stack.pop(0)
              
            if node1==None and node2==None:
                continue
            
            if node1 == None and node2 is not None:
                return False
            
            if node1 is not None and node2 is None:
                return False
            
            if node1.val != node2.val:
                return False
            
            stack.append((node1.left, node2.left))
            stack.append((node1.right, node2.right))
            
                     
        return True


#Solution - Recursive


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        
        if p is None and q is not None:
            return False
        
        if p is not None and q is None:
            return False
        
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)