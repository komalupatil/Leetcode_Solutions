#Leetcode 404. Sum of Left Leaves

#DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
            
        ans = 0
        if root.left != None and root.left.left == None and root.left.right == None:
            ans += root.left.val       

        ans += self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        return ans

#BFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution2:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        queue = deque()  
        queue.append(root)  
        result = 0  
        while queue:
            currentNode = queue.popleft()
            if currentNode.left:
                queue.append(currentNode.left)
                if not currentNode.left.left and not currentNode.left.right:
                    result += currentNode.left.val
            if currentNode.right:
                queue.append(currentNode.right)
        return result
        