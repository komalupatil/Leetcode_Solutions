#Leetcode 257. Binary Tree Paths


#Given a binary tree, return all root-to-leaf paths.
#Note: A leaf is a node with no children.



#Solution


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        allPaths = [] 
        self.findPaths(root, "", allPaths)
        return allPaths
    
    def findPaths(self, root, currentPath, allPaths):
        if root == None:
            return None
        
        currentPath += str(root.val)
        
        if root.left == None and root.right == None:
            allPaths.append(currentPath)
        
        else:
            currentPath += "->"
            self.findPaths(root.left, currentPath, allPaths)
            self.findPaths(root.right, currentPath, allPaths)
        