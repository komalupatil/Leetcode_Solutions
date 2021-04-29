#Leetcode 226. Invert Binary Tree

#BFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        queue = deque()

        queue.append(root)
        
        while queue:
            current = queue.popleft()
            temp = current.left
            current.left = current.right
            current.right = temp
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return root

#DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root