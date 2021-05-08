#Leetcode 104. Maximum Depth of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution1:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        return 1 + max(left, right)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        queue = deque()
        queue.append(root)
        
        maxDepth = 0
        while queue:
            
            levelSize = len(queue)
            for _ in range(levelSize):
                currentNode = queue.popleft()
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            maxDepth += 1
        return maxDepth