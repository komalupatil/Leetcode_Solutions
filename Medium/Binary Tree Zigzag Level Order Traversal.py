#Leetcode 103. Binary Tree Zigzag Level Order Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution1:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []        
        queue = deque([root])
        flag = 1
        while queue: 
            currentLevel = []
            for _ in range(len(queue)):
                currentNode = queue.popleft()
                currentLevel.append(currentNode.val)
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            result.append(currentLevel[::flag])
            flag *= -1
        return result

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if not root:
            return result
        
        queue = deque()
        queue.append(root)
        leftToRight = True
        while queue:
            levelSize = len(queue)
            currentLevel = []
            for _ in range(levelSize): 
                currentNode = queue.popleft()
                if leftToRight:
                    currentLevel.append(currentNode.val)
                else:
                    currentLevel.insert(0,currentNode.val)
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            leftToRight = not leftToRight
            result.append(currentLevel)
        return result