#Leetcode 199. Binary Tree Right Side View

#Solution - BFS approach
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        result = []
        if root is None:
            return result
        
        queue = deque()
        queue.append(root)
        
        while queue:
            levelsize = len(queue)           
            for _ in range(levelsize):
                currentNode = queue.popleft()
                val = currentNode.val
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            result.append(val)
                
        return result