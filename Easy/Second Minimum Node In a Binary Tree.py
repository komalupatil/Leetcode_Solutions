#Leetcode 671. Second Minimum Node In a Binary Tree

#DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        
        
        def dfs(node):
            if not node:
                return
            if min1<node.val<self.ans:
                self.ans = node.val
            dfs(node.left)
            dfs(node.right)
            
        self.ans = float('inf')
        min1 = root.val
        dfs(root)
        
        if self.ans == float('inf'):
            return -1 
        else:
            return self.ans 

#BFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root:
            return -1
        
        queue = deque()
        queue.append(root)
        
        min1 = root.val
        minimum = float('inf')
        
        while queue:
            node = queue.popleft()
            if node.val < minimum and node.val != min1:
                minimum = node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
        if minimum == float('inf'):
            return -1
        return minimum