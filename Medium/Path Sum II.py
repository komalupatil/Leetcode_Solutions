#Leetcode 113. Path Sum II

#Given a binary tree and a sum, find all root-to-leaf paths 
#where each path's sum equals the given sum.

#Note: A leaf is a node with no children.


#Solution

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root == None:
            return None
        allPaths = []
        self.findPaths(root, sum, [], allPaths)
        return allPaths
        
    def findPaths(self, root, sum, currentPath, allPaths):
        if root == None:
            return None
        
        sum -= root.val
        currentPath.append(root.val)
        
        if root.left == None and root.right==None and sum == 0:
            allPaths.append(currentPath)
        
        else: 
            self.findPaths(root.left, sum, currentPath[:], allPaths)
            self.findPaths(root.right, sum, currentPath[:], allPaths)
        