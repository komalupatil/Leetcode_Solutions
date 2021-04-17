#Leetcode 404. Sum of Left Leaves

#Solution - DFS recursive

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        ans = 0
        if not root:
            return 0
        
        if root.left != None and root.left.left == None and root.left.right == None:
            ans += root.left.val 
        
        
        
        ans += self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        
        return ans


#Solution - BFS recursive

