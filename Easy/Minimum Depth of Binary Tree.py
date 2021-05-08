#Leetcode 111. Minimum Depth of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        queue = deque()
        queue.append(root)
        minimumTreeDepth = 0
        while queue:
            minimumTreeDepth += 1
            levelSize = len(queue)
            for _ in range(levelSize):
                currentNode = queue.popleft()

                # check if this is a leaf node
                if not currentNode.left and not currentNode.right:
                    return minimumTreeDepth

                # insert the children of current node in the queue
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left or not root.right:
            return self.minDepth(root.left)+self.minDepth(root.right)+1
        return min(self.minDepth(root.right),self.minDepth(root.left))+1