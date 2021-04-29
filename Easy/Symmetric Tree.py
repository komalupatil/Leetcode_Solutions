#Leetcode 101. Symmetric Tree

#DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        
        return self.isMirror(root, root)
    
    def isMirror(self, p, q):
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        return p.val == q.val and self.isMirror(p.right, q.left) and self.isMirror(p.left, q.right)

#BFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        
        queue = deque()
        queue.append(root)
        queue.append(root)
        
        while queue:
            p = queue.popleft()
            q = queue.popleft()
            
            if p == None and q == None:
                continue
            if p == None or q == None:
                return False
            if p.val != q.val:
                return False
            queue.append(p.right)
            queue.append(q.left)
            queue.append(p.left)
            queue.append(q.right)
        return True