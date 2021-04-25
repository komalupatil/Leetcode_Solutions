#Leetcode 637. Average of Levels in Binary Tree


#Solution - BFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        queue = deque()
        queue.append(root)
        result = []        
        
        while queue:
            levelSum = 0
            levelSize = len(queue)            
            for _ in range(levelSize):
                currentNode = queue.popleft()
                levelSum += currentNode.val
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)                
            result.append(levelSum/levelSize)
        return result